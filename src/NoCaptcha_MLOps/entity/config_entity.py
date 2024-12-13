from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestion:
    root_dir: Path

@dataclass
class DataPreprocessing:
    root_dir: Path
    test_data_path: Path
    train_data_path: Path
    test_size: float
    preprocess_model_save_path: Path

@dataclass
class DataTraining:
    root_dir: Path
    test_data_path: Path
    train_data_path: Path
    test_size: float
    model_dir: Path

@dataclass
class Prediction:
    model_path: Path
    preprocessor_path: Path
