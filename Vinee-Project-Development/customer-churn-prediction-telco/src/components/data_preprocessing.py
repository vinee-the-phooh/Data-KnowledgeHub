import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from logger.logger import logger
from exception.exception import CustomException
from src.config import TARGET_COL

class DataPreprocessing:
    def __init__(self, test_size: float = 0.2, random_state: int = 42):
        self.test_size = test_size
        self.random_state = random_state

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            df = df.copy()

            # 1) Drop ID column (Because it is not useful for prediction)
            if "customerID" in df.columns:
                df.drop(columns=["customerID"], inplace=True)
                logger.info("Dropped column: customerID")

            # 2) Fix TotalCharges (it often comes as string with blanks)
            if "TotalCharges" in df.columns:
                df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
                df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())
                logger.info("Filled missing TotalCharges with median")

            # 3) Encode target (Yes/No -> 1/0)
            if TARGET_COL in df.columns:
                df[TARGET_COL] = df[TARGET_COL].map({"Yes": 1, "No": 0})
                logger.info("Encoded target Churn: Yes->1, No->0")

            return df

        except Exception as e:
            raise CustomException(e, sys)

    def split_data(self, df: pd.DataFrame):
        try:
            if TARGET_COL not in df.columns:
                raise ValueError(f"Target column '{TARGET_COL}' not found.")

            X = df.drop(columns=[TARGET_COL])
            y = df[TARGET_COL]

            X_train, X_test, y_train, y_test = train_test_split(
                X, y,
                test_size=self.test_size,
                random_state=self.random_state,
                stratify=y
            )

            logger.info(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")
            return X_train, X_test, y_train, y_test

        except Exception as e:
            raise CustomException(e, sys)