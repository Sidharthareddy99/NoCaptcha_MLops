from src.NoCaptcha_MLOps.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.NoCaptcha_MLOps.utils.common import read_yaml,create_directories
from src.NoCaptcha_MLOps.entity.config_entity import DataIngestion, DataPreprocessing, DataTraining, Prediction


class ConfigManager:
    def __init__(self, config_file_path= CONFIG_FILE_PATH):
        self.config = read_yaml(config_file_path)
        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestion:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestion(
            root_dir= config.root_dir
            )
        return data_ingestion_config
    
    def get_data_preprocessing_config(self) -> DataPreprocessing:
        config = self.config.data_preprocessing
        #create_directories([config.root_dir])

        data_preprocessing_config = DataPreprocessing(
            root_dir= config.root_dir,
            test_data_path= config.test_data_path,
            train_data_path= config.train_data_path,
            test_size= config.test_size,
            preprocess_model_save_path= config.preprocess_model_save_path
        )
        return data_preprocessing_config

    def get_data_training_config(self) -> DataTraining:
        config = self.config.data_training

        data_preprocessing_config = DataTraining(
            root_dir= config.root_dir,
            test_data_path= config.test_data_path,
            train_data_path= config.train_data_path,
            test_size= config.test_size,
            model_dir= config.model_dir
        )
        return data_preprocessing_config
    
    def get_prediction_config(self):
        config = self.config.prediction
        data_preprocessing_config = Prediction(
            model_path= config.model_path,
            preprocessor_path= config.preprocessor_path
        )
        return data_preprocessing_config



