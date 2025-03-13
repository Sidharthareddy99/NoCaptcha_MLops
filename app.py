from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.NoCaptcha_MLOps.pipeline.prediction_pipeline import PredictionPipeline
from src.NoCaptcha_MLOps.pipeline.training_pipeline import DataIngestionPipeline, DataPreprocessingPipeline, DataTrainingPipeline
import numpy as np
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
prediction_pipeline = PredictionPipeline()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PredictionInput(BaseModel):
    Mouse_Path_Length: float
    Mouse_Avg_Speed: float
    Mouse_Max_Speed: float
    Mouse_Stops: int
    Mouse_Click_Frequency: float
    Mouse_Scroll_Speed: float
    Mouse_Scroll_Direction_Changes: int
    Avg_Click_X: float
    Avg_Click_Y: float
    Click_Spread: float
    Typing_Speed: float
    Keypress_Interval_Avg: float
    Key_Hold_Duration_Avg: float
    Special_Key_Usage: int
    Error_Corrections: int
    Pause_Between_Typing: float
    Interaction_Duration: float
    Mouse_Keyboard_Interaction_Correlation: float
    Response_Time: float

@app.post("/predict")
async def predict(input_data: PredictionInput):
    try:
        # Convert input data to dictionary
        input_data_dict = input_data.model_dump()

        # Run the prediction pipeline
        predictions = prediction_pipeline.run(input_data_dict)

        # Convert predictions to a serializable format
        if isinstance(predictions, np.ndarray):
            predictions = predictions.tolist()

        return JSONResponse(content={"predictions": predictions})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/train")
async def train():
    try:
        # Run the training pipeline
        dataIngestion = DataIngestionPipeline()
        dataIngestion.data_ingestion()

        dataPreprocessing = DataPreprocessingPipeline()
        dataPreprocessing.data_preprocessing()

        dataTraining = DataTrainingPipeline()
        dataTraining.data_training()
        return JSONResponse(content={"message": "Training pipeline completed successfully"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)