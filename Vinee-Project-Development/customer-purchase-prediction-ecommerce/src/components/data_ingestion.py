import sys
import pandas as pd

from logger.logger import logger
from exception.exception import CustomException
from src.config import DATA_RAW_DIR, RAW_FILE_NAME

class DataIngestion:
    def load_data(self) -> pd.DataFrame:
        try:
            file_path = DATA_RAW_DIR / RAW_FILE_NAME

            if not file_path.exists():
                raise FileNotFoundError(f"Dataset not found at {file_path}")

            df = pd.read_csv(file_path)

            logger.info(f"Dataset loaded successfully. Shape: {df.shape}")
            logger.info(f"Columns: {list(df.columns)}")

            return df

        except Exception as e:
            raise CustomException(e, sys)