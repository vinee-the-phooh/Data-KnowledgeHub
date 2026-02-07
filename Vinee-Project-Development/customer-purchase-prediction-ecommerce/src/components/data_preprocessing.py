import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from logger.logger import logger
from exception.exception import CustomException
from src.config import TARGET_COL, TEST_SIZE, RANDOM_STATE

class DataPreprocessing:
    def clean_and_split(self, df: pd.DataFrame):
        try:
            df = df.copy()

            # 1. Drop ID column
            if "user_id" in df.columns:
                df.drop(columns=["user_id"], inplace=True)
                logger.info("Dropped column: user_id")

            # 2. Split features & target
            X = df.drop(columns=[TARGET_COL])
            y = df[TARGET_COL]

            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=TEST_SIZE,
                random_state=RANDOM_STATE,
                stratify=y
            )

            logger.info(
                f"Train shape: {X_train.shape}, Test shape: {X_test.shape}"
            )

            return X_train, X_test, y_train, y_test

        except Exception as e:
            raise CustomException(e, sys)