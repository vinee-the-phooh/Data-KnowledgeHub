import sys
import pandas as pd
from sklearn.datasets import fetch_california_housing
from logger.logger import logger
from exception.exception import CustomException
from src.config import TARGET_COL

class DataIngestion:
    def load_data(self) -> pd.DataFrame:
        try:
            logger.info("Loading California Housing dataset from sklearn")

            data = fetch_california_housing(as_frame=True)
            df = data.frame

            logger.info(f"Dataset loaded. Shape: {df.shape}")
            logger.info(f"Target column: {TARGET_COL}")
            logger.info(f"Columns in dataset: {list(df.columns)}")

            return df

        except Exception as e:
            raise CustomException(e, sys)