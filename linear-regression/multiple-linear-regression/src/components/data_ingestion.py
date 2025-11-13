import os
import sys
import pandas as pd
from logger.logger import logging
from exception.exception import CustomException

"""
Load dataset
Log shape and columns
Log missing values and duplicates
"""
class DataIngestion:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def initiate_data_ingestion(self):
        logging.info("======= Data Ingestion Started =======")
        try:
            if not os.path.exists(self.file_path):
                raise CustomException(f"File not found at path: {self.file_path}", sys)

            
            df = pd.read_csv(self.file_path)
            logging.info(f"Dataset loaded successfully from {self.file_path}")

            
            logging.info(f"Dataset Shape: {df.shape}")
            logging.info(f"Columns: {list(df.columns)}")

            
            missing = df.isnull().sum().sum()
            duplicates = df.duplicated().sum()
            logging.info(f"Missing Values Count: {missing}")
            logging.info(f"Duplicate Rows Count: {duplicates}")

            logging.info("======= Data Ingestion Completed =======")
            return df

        except Exception as e:
            logging.error("Error occurred during data ingestion")
            raise CustomException(e, sys)