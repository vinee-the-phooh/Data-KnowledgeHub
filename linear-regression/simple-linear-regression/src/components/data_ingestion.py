import os
import pandas as pd
from src.logger import logging
from src.exception import CustomException

"""
Reads raw dataset, and saves a copy to the processed data folder.
"""

class DataIngestion:
    def __init__(self, raw_data_path: str, processed_data_path: str):
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path

    def initiate_data_ingestion(self):
        
        logging.info("==== Data Ingestion process started ====")

        try:
            
            if not os.path.exists(self.raw_data_path):
                logging.error(f"Raw data file not found at: {self.raw_data_path}")
                raise CustomException(f"File not found: {self.raw_data_path}")
            
            df = pd.read_csv(self.raw_data_path)
            logging.info(f"Dataset loaded successfully with shape {df.shape}")

            os.makedirs(os.path.dirname(self.processed_data_path), exist_ok=True)
            df.to_csv(self.processed_data_path, index=False)
            logging.info(f"Dataset copy saved to {self.processed_data_path}")

            logging.info("==== Data Ingestion process completed successfully ====")
            return df

        except Exception as e:
            logging.error("Error occurred during data ingestion.")
            raise CustomException(e)