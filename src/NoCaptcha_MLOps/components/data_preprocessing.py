# FILE: src/NoCaptcha_MLOps/components/data_preprocessing.py

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import joblib
from src.NoCaptcha_MLOps.entity.config_entity import DataPreprocessing

class DataPreprocessingPipeline:    
    def __init__(self, config: DataPreprocessing):
        self.config = config
        self.root_data_path = config.root_dir
        self.train_data_path = config.train_data_path
        self.test_data_path = config.test_data_path
        self.test_size = config.test_size
        self.preprocessor_save_path = config.preprocess_model_save_path
        os.makedirs(os.path.dirname(self.train_data_path), exist_ok=True)
        os.makedirs(os.path.dirname(self.test_data_path), exist_ok=True)
        os.makedirs(os.path.dirname(self.preprocessor_save_path), exist_ok=True)
    
    def load_data(self):
        print("Loading data...")
        data = pd.read_csv(self.root_data_path)
        self.Lables = data.columns
        return data
    
    def preprocess_data(self):
        print("Starting Data Preprocessing Pipeline...")
        data = self.load_data()

        # Drop unnecessary columns
        data.drop("_id", axis=1, inplace=True)
        data.drop("Mouse_Scroll_Speed", axis=1, inplace=True)
        data.drop("Mouse_Scroll_Direction_Changes", axis=1, inplace=True)
        data.drop("Error_Corrections", axis=1, inplace=True)
        data.drop("Response_Time", axis=1, inplace=True)

        # Separate features and target
        X = data.drop("Result", axis=1)
        y = data["Result"]

        # Replace zero values in numerical columns with np.nan for proper imputation
        numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
        X[numerical_cols] = X[numerical_cols].replace(0, np.nan)
        
        # Identify categorical columns
        categorical_cols = X.select_dtypes(include=['object']).columns

        # Preprocessing for numerical data
        numerical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])
        
        # Preprocessing for categorical data
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])
        
        # Bundle preprocessing for numerical and categorical data
        preprocessor = ColumnTransformer(
            transformers=[
                ('numerical', numerical_transformer, numerical_cols),
                ('categorical', categorical_transformer, categorical_cols)
            ],
            remainder='passthrough',  # Keep all other columns as they are
            verbose_feature_names_out=False  # Prevent prefixing feature names
        )
        
        # Preprocessing pipeline
        pipeline = Pipeline(steps=[('preprocessor', preprocessor)])
        
        # Fit and transform the data
        X_preprocessed = pipeline.fit_transform(X)
        
        # Save the preprocessing pipeline
        joblib.dump(pipeline, self.preprocessor_save_path)
        print(f"Preprocessing pipeline saved to {self.preprocessor_save_path}")
        
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=self.test_size, random_state=42)
        actual_train_data, actual_test_data = train_test_split(data, test_size=self.test_size, random_state=42)


        # Get feature names after transformation
        feature_names = preprocessor.get_feature_names_out()

        # Convert the numpy arrays back to pandas DataFrames
        train_data = pd.DataFrame(X_train, columns=feature_names)
        train_data['Result'] = y_train.reset_index(drop=True)
    

        # Save the splits to separate files
        train_data.to_csv(self.train_data_path, index=False)
        actual_test_data.to_csv(self.test_data_path, index=False)
        
        print("Data Preprocessing Pipeline completed.")
