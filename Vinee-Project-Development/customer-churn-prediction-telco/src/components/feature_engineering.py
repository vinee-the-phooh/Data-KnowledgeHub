import sys
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

from exception.exception import CustomException
from logger.logger import logger

class FeatureEngineering:
    def __init__(self):
        pass

    def build_transformer(self, X: pd.DataFrame) -> ColumnTransformer:
        try:
            numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
            categorical_cols = X.select_dtypes(include=["object", "bool"]).columns.tolist()

            logger.info(f"Numeric cols: {len(numeric_cols)}, Categorical cols: {len(categorical_cols)}")

            numeric_pipe = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            categorical_pipe = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore"))
            ])

            transformer = ColumnTransformer(
                transformers=[
                    ("num", numeric_pipe, numeric_cols),
                    ("cat", categorical_pipe, categorical_cols)
                ]
            )

            return transformer

        except Exception as e:
            raise CustomException(e, sys)