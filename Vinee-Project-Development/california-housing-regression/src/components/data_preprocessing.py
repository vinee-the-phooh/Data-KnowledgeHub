import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from logger.logger import logger
from exception.exception import CustomException
from src.config import TARGET_COL, TEST_SIZE, RANDOM_STATE

class DataPreprocessing:
    def split_and_scale(self, df: pd.DataFrame):
        try:
            X = df.drop(columns=[TARGET_COL])
            y = df[TARGET_COL]

            X_train, X_test, y_train, y_test = train_test_split(
                X, y,
                test_size=TEST_SIZE,
                random_state=RANDOM_STATE
            )

            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            logger.info("Data split and feature scaling completed")

            return X_train_scaled, X_test_scaled, y_train, y_test

        except Exception as e:
            raise CustomException(e, sys)