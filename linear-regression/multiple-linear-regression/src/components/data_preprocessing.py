import os
import sys
import numpy as np
import pandas as pd
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from logger.logger import logging
from exception.exception import CustomException

"""
Remove duplicate rows
Handle missing values (numeric -> median, categorical->mode)
Handle outliers using IQR (for numeric cols except target)
Build preprocessing pipeline (encoding + scaling) and transform
Save preprocessor for future use (training)
Save cleaned (pre-encoded) dataframe for reference
"""

class DataPreprocessor:
    def __init__(self, df: pd.DataFrame, target_col: str = "Units_Sold"):
        self.df = df.copy()
        self.target_col = target_col
        self.processed_data_dir = "data/processed"
        self.models_dir = "models"
        os.makedirs(self.processed_data_dir, exist_ok=True)
        os.makedirs(self.models_dir, exist_ok=True)

    
    def remove_duplicates(self):
        try:
            logging.info("======= Preprocessing: Remove Duplicates Started =======")
            before = self.df.shape[0]
            self.df.drop_duplicates(inplace=True)
            after = self.df.shape[0]
            logging.info(f"Duplicates removed: {before - after}")
            logging.info("======= Preprocessing: Remove Duplicates Completed =======")
        except Exception as e:
            raise CustomException(e, sys)

    
    def handle_missing_values(self):
        try:
            logging.info("======= Preprocessing: Handle Missing Values Started =======")

            num_cols = self.df.select_dtypes(include=["int64", "float64"]).columns.tolist()
            cat_cols = self.df.select_dtypes(include=["object"]).columns.tolist()

            if self.target_col in num_cols:
                num_cols.remove(self.target_col)

            # Numeric: median
            for col in num_cols:
                if self.df[col].isnull().sum() > 0:
                    median_val = self.df[col].median()
                    self.df[col].fillna(median_val, inplace=True)
                    logging.info(f"Filled missing values in numeric column '{col}' with median: {median_val}")

            # Categorical: mode
            for col in cat_cols:
                if self.df[col].isnull().sum() > 0:
                    mode_val = self.df[col].mode()[0]
                    self.df[col].fillna(mode_val, inplace=True)
                    logging.info(f"Filled missing values in categorical column '{col}' with mode: {mode_val}")

            logging.info("======= Preprocessing: Handle Missing Values Completed =======")

        except Exception as e:
            raise CustomException(e, sys)

    
    def handle_outliers_iqr(self):
        try:
            logging.info("======= Preprocessing: Outlier Treatment Started =======")

            num_cols = self.df.select_dtypes(include=["int64", "float64"]).columns.tolist()
            if self.target_col in num_cols:
                num_cols.remove(self.target_col)

            for col in num_cols:
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                # This technique is called Winsorization — instead of removing outliers, we cap them to boundary values.
                # It helps to keep the dataset size same and makes it more robust for regression.
                outliers = ((self.df[col] < lower_bound) | (self.df[col] > upper_bound)).sum()
                if outliers > 0:
                    self.df[col] = np.where(self.df[col] < lower_bound, lower_bound, self.df[col])
                    self.df[col] = np.where(self.df[col] > upper_bound, upper_bound, self.df[col])
                    logging.info(f"Outliers capped in column '{col}'. Count: {outliers}")

            logging.info("======= Preprocessing Outlier Completed =======")

        except Exception as e:
            raise CustomException(e, sys)

   
    def apply_transformations(self):
        try:
            logging.info("======= Preprocessing: Apply Transformations Started =======")

            if self.target_col not in self.df.columns:
                raise CustomException(f"Target column '{self.target_col}' not found in dataframe.", sys)

            X = self.df.drop(columns=[self.target_col])
            y = self.df[self.target_col]

            numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
            categorical_features = X.select_dtypes(include=["object"]).columns.tolist()

            logging.info(f"Numeric Features: {numeric_features}")
            logging.info(f"Categorical Features: {categorical_features}")

            numeric_transformer = StandardScaler()
            categorical_transformer = OneHotEncoder(handle_unknown="ignore")

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num", numeric_transformer, numeric_features),
                    ("cat", categorical_transformer, categorical_features),
                ]
            )

            X_processed = preprocessor.fit_transform(X)

            
            preprocessor_path = os.path.join(self.models_dir, "preprocessor.pkl")
            with open(preprocessor_path, "wb") as f:
                pickle.dump(preprocessor, f)
            logging.info(f"Preprocessor saved at: {preprocessor_path}")
            
            cleaned_path = os.path.join(self.processed_data_dir, "cleaned_data.csv")
            self.df.to_csv(cleaned_path, index=False)
            logging.info(f"Cleaned data saved at: {cleaned_path}")

            logging.info("======= Preprocessing: Apply Transformations Completed =======")

            return X_processed, y

        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_preprocessing(self):
        logging.info("======= Data Preprocessing Pipeline Started =======")
        self.remove_duplicates()
        self.handle_missing_values()
        self.handle_outliers_iqr()
        X_processed, y = self.apply_transformations()
        logging.info("======= Data Preprocessing Pipeline Completed =======")
        return X_processed, y