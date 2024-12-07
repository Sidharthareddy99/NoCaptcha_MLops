from src.NoCaptcha_MLOps.config.configuration import ConfigManager
from src.NoCaptcha_MLOps.components.predict import PredictionPipeline as PredictionComponentPipeline

class PredictionPipeline:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.prediction_config = self.config_manager.get_prediction_config()
        self.prediction = PredictionComponentPipeline(self.prediction_config)
    
    def run(self, input_data):
        config_manager = ConfigManager()
        prediction_config = config_manager.get_prediction_config()

        prediction_pipeline = PredictionComponentPipeline(prediction_config)
        predictions = prediction_pipeline.run_pipeline(input_data)
        return predictions