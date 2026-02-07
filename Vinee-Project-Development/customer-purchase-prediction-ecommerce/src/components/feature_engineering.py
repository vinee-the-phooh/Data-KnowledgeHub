import sys
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

from logger.logger import logger
from exception.exception import CustomException

class FeatureEngineering:
    def build_transformer(self, X: pd.DataFrame):
        try:
            numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
            categorical_cols = X.select_dtypes(include=["object", "bool"]).columns.tolist()

            logger.info(f"Numeric cols: {numeric_cols}")
            logger.info(f"Categorical cols: {categorical_cols}")

            numeric_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehot", OneHotEncoder(handle_unknown="ignore"))
                ]
            )

            transformer = ColumnTransformer(
                transformers=[
                    ("num", numeric_pipeline, numeric_cols),
                    ("cat", categorical_pipeline, categorical_cols)
                ]
            )

            return transformer

        except Exception as e:
            raise CustomException(e, sys)