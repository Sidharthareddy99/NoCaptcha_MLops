from src.NoCaptcha_MLOps.config.configuration import ConfigManager
from src.NoCaptcha_MLOps.components.data_ingestion import DataIngestion
from src.NoCaptcha_MLOps.components.data_preprocessing import DataPreprocessingPipeline as DataPreprocessingComponentPipeline
from src.NoCaptcha_MLOps.components.data_training import ModelBuildingPipeline as ModelBuildingPipeline
from dagshub import get_repo_bucket_client

class DataIngestionPipeline:
    def data_ingestion(self):
        print("Starting Data Ingestion Pipeline...")
        self.config_manager = ConfigManager()
        self.data_ingestion_config = self.config_manager.get_data_ingestion_config()
        self.data_ingestion = DataIngestion(self.data_ingestion_config)
        self.data_ingestion.run()
    

class DataPreprocessingPipeline: 
    def data_preprocessing(self):
        print("Starting Data Preprocessing Pipeline...")
        self.config_manager = ConfigManager()
        self.data_preprocessing_config = self.config_manager.get_data_preprocessing_config()
        self.preprocessing = DataPreprocessingComponentPipeline(self.data_preprocessing_config)
        self.preprocessing.preprocess_data()

class DataTrainingPipeline:
    def data_training(self):
        print("Starting Data Training Pipeline...")
        self.config_manager = ConfigManager()
        self.data_training_config = self.config_manager.get_data_training_config()
        self.training = ModelBuildingPipeline(self.data_training_config)
        self.training.run_pipeline()

        # Upload artifacts to DagsHub S3 bucket
        s3 = get_repo_bucket_client("Sidharthareddy99/NoCaptcha_MLops")
        
        s3.upload_file(
            Bucket="NoCaptcha_MLops",  # name of the repo
            Filename="artifacts/training/model/model.joblib",  # local path of file to upload
            Key="artifacts/training/model/model.joblib"  # remote path where to upload the file
        )

