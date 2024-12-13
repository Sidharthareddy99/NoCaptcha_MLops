import pymongo
import pandas as pd
from src.NoCaptcha_MLOps.entity.config_entity import DataIngestion
from dotenv import load_dotenv
import os
load_dotenv()

class DataIngestion:
    def __init__(self, config: DataIngestion):
        self.MONGO_URI = os.getenv("MONGO_URI")
        self.DATABASE_NAME = os.getenv("DATABASE_NAME")
        self.COLLECTION_NAME = os.getenv("COLLECTION_NAME")
        self.config = config
        self.root_dir = config.root_dir
        self.client = pymongo.MongoClient(self.MONGO_URI)
        self.database = self.client[self.DATABASE_NAME]
        self.collection = self.database[self.COLLECTION_NAME]
    
    def fetch_data_from_mongodb(self):
        # Fetch all documents from the MongoDB collection
        data = list(self.collection.find())
        
        # Normalize MongoDB data to remove MongoDB-specific types
        for record in data:
            record["_id"] = str(record["_id"])  # Convert ObjectId to string
            for key, value in record.items():
                if isinstance(value, dict) and "$numberDouble" in value:
                    record[key] = float(value["$numberDouble"])
                elif isinstance(value, dict) and "$numberInt" in value:
                    record[key] = int(value["$numberInt"])
        
        return data

    def convert_data_to_csv(self, data, file_path="artifacts/data_ingestion/data.csv"):
        # Convert the data to a Pandas DataFrame
        df = pd.DataFrame(data)
        # Save to a CSV file
        df.to_csv(file_path, index=False)
        print(f"Data successfully saved to {file_path}")
        

    def run(self):
        print("Fetching data from MongoDB...")
        data = self.fetch_data_from_mongodb()
        print("Converting data to CSV...")
        self.convert_data_to_csv(data)
