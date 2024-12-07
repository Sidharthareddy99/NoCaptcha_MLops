# FILE: src/NoCaptcha_MLOps/components/predict.py

import pandas as pd
import numpy as np
import joblib
from src.NoCaptcha_MLOps.config.configuration import Prediction
from sklearn.compose import ColumnTransformer

class PredictionPipeline:
    def __init__(self, config: Prediction):
        self.config = config
        self.model_path = config.model_path
        self.preprocessor_path = config.preprocessor_path
        self.model = self.load_model()
        self.preprocessor = self.load_preprocessor()
        self.feature_names = self.get_feature_names()

    def load_model(self):
        print(f"Loading model from {self.model_path}...")
        model = joblib.load(self.model_path)
        return model

    def load_preprocessor(self):
        print(f"Loading preprocessor from {self.preprocessor_path}...")
        preprocessor = joblib.load(self.preprocessor_path)
        return preprocessor

    def get_feature_names(self):
        feature_names = []
        for name, step in self.preprocessor.steps:
            if isinstance(step, ColumnTransformer):
                feature_names = step.get_feature_names_out()
                break
        return feature_names

    def preprocess_data(self, data):
        print("Preprocessing input data...")
        data = pd.DataFrame([data])
        missing_cols = set(self.feature_names) - set(data.columns)
        print(f"Missing columns: {missing_cols}")   
        for col in missing_cols:
            data[col] = np.nan
        data = data[self.feature_names]
        data.columns = self.feature_names
        preprocessed_data = self.preprocessor.transform(data)
        return preprocessed_data

    def predict(self, data):
        print("Making predictions...")
        preprocessed_data = self.preprocess_data(data)
        print(f"Preprocessed data shape: {preprocessed_data.shape}")
        predictions = self.model.predict(preprocessed_data)
        return predictions

    def run_pipeline(self, input_data):
        print(f"Running prediction pipeline...")
        predictions = self.predict(input_data)
        return predictions