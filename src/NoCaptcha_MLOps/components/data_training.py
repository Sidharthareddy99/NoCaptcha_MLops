import os
import dagshub.auth
import dagshub.auth.token_auth
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import mlflow
import mlflow.sklearn
import dagshub
dagshub.auth.add_app_token(token='3d3040aeacd891d2b4577b5aa843fafb22081517')
dagshub.init(repo_owner='Sidharthareddy99', repo_name='NoCaptcha_MLops', mlflow=True)


class ModelBuildingPipeline:
    def __init__(self, config):
        self.config = config
        self.train_data_path = config.train_data_path
        self.test_data_path = config.test_data_path
        self.test_size = config.test_size
        self.model_save_path = config.model_dir
        os.makedirs(os.path.dirname(self.train_data_path), exist_ok=True)
        os.makedirs(os.path.dirname(self.test_data_path), exist_ok=True)
        os.makedirs(self.model_save_path, exist_ok=True)

    def load_data(self):
        print("Loading data...")
        data = pd.read_csv(self.train_data_path)
        return data

    def preprocess_data(self, data):
        print("Starting Data Preprocessing...")
        # Separate features and target
        X = data.drop("Result", axis=1)
        y = data["Result"]
        return X, y

    def split_data(self, X, y):
        print("Splitting data into train and test sets...")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=42)
        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        print("Training model with hyperparameter tuning...")
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
        model = RandomForestClassifier(random_state=42)
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
        print("Input data size : ", X_train.shape)
        grid_search.fit(X_train, y_train)
        print(f"Best parameters found: {grid_search.best_params_}")
        best_model = grid_search.best_estimator_
        return best_model

    def evaluate_model(self, model, X_test, y_test):
        print("Evaluating model on internal Data...")
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        print(f"Accuracy: {accuracy}")
        print(f"Classification Report:\n{report}")
        return accuracy, report

    def save_model(self, model):
        print(f"Saving model to {self.config.model_dir}...")
        os.makedirs(self.config.model_dir, exist_ok=True)
        model_path = os.path.join(self.config.model_dir, "model.joblib")
        joblib.dump(model, model_path)
        print(f"Model saved to {model_path}")

        # Log the model with MLflow
        mlflow.sklearn.log_model(model, "model")

    def run_pipeline(self):
        mlflow.set_experiment("ModelBuildingExperiment")
        with mlflow.start_run():
            data = self.load_data()
            X, y = self.preprocess_data(data)
            X_train, X_test, y_train, y_test = self.split_data(X, y)
            model = self.train_model(X_train, y_train)
            accuracy, report = self.evaluate_model(model, X_test, y_test)
            self.save_model(model)

            # Log parameters
            mlflow.log_params({
                "train_data_path": self.train_data_path,
                "test_data_path": self.test_data_path,
                "test_size": self.test_size,
                "model_save_path": self.model_save_path
            })

            # Log best model parameters
            best_params = model.get_params()
            mlflow.log_params(best_params)

            # Log metrics
            mlflow.log_metric("accuracy", accuracy)

            print("Model building pipeline completed!")