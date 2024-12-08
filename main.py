from src.NoCaptcha_MLOps.pipeline.training_pipeline import DataIngestionPipeline, DataPreprocessingPipeline, DataTrainingPipeline
from src.NoCaptcha_MLOps.pipeline.prediction_pipeline import PredictionPipeline


# dataIngestion = DataIngestionPipeline()
# dataIngestion.data_ingestion()

# dataPreprocessing = DataPreprocessingPipeline()
# dataPreprocessing.data_preprocessing()

dataTraining = DataTrainingPipeline()
dataTraining.data_training()

# prediction = PredictionPipeline()
# prediction.run("artifacts/data_preprocessing/test.csv")