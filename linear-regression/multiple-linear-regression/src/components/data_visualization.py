import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from logger.logger import logging
from exception.exception import CustomException

class DataVisualization:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.save_dir = "reports/eda"
        os.makedirs(self.save_dir, exist_ok=True)

    def perform_basic_checks(self):
        try:
            logging.info("======= EDA: Basic Info Started =======")
            logging.info(f"Data Shape: {self.df.shape}")
            logging.info(f"Columns: {list(self.df.columns)}")
            logging.info(f"Data Types:\n{self.df.dtypes}")
            logging.info(f"Missing Values:\n{self.df.isnull().sum()}")
            logging.info(f"Duplicate Rows: {self.df.duplicated().sum()}")
            logging.info("======= EDA: Basic Info Completed =======")

        except Exception as e:
            raise CustomException(e, sys)

    def plot_missing_values(self):
        try:
            logging.info("Plotting missing value heatmap...")
            plt.figure(figsize=(10, 6))
            sns.heatmap(self.df.isnull(), cbar=False, cmap='viridis')
            plt.title("Missing Values Heatmap")
            plt.tight_layout()
            file_path = os.path.join(self.save_dir, "missing_values_heatmap.png")
            plt.savefig(file_path)
            plt.close()
            logging.info(f"Missing values heatmap saved at {file_path}")

        except Exception as e:
            raise CustomException(e, sys)

    def plot_distributions(self):
        try:
            logging.info("Plotting feature distributions...")
            numeric_cols = self.df.select_dtypes(include=['int64', 'float64']).columns
            for col in numeric_cols:
                plt.figure(figsize=(8, 5))
                sns.histplot(self.df[col].dropna(), kde=True, bins=30)
                plt.title(f"Distribution of {col}")
                plt.tight_layout()
                file_path = os.path.join(self.save_dir, f"{col}_distribution.png")
                plt.savefig(file_path)
                plt.close()
                logging.info(f"Distribution plot saved for column: {col}")

        except Exception as e:
            raise CustomException(e, sys)

    def plot_correlation_heatmap(self):
        try:
            logging.info("Plotting correlation heatmap...")
            numeric_df = self.df.select_dtypes(include=['int64', 'float64'])
            plt.figure(figsize=(10, 8))
            sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
            plt.title("Correlation Heatmap")
            plt.tight_layout()
            file_path = os.path.join(self.save_dir, "correlation_heatmap.png")
            plt.savefig(file_path)
            plt.close()
            logging.info(f"Correlation heatmap saved at {file_path}")

        except Exception as e:
            raise CustomException(e, sys)

    def plot_categorical_counts(self):
        try:
            logging.info("Plotting categorical column distributions...")
            cat_cols = self.df.select_dtypes(include=['object']).columns
            for col in cat_cols:
                plt.figure(figsize=(8, 5))
                sns.countplot(data=self.df, x=col)
                plt.title(f"Count of {col}")
                plt.tight_layout()
                file_path = os.path.join(self.save_dir, f"{col}_countplot.png")
                plt.savefig(file_path)
                plt.close()
                logging.info(f"Categorical count plot saved for column: {col}")
        except Exception as e:
            raise CustomException(e, sys)

    def plot_feature_vs_target(self, target_col="Units_Sold"):
        try:
            numeric_cols = self.df.select_dtypes(include=['int64', 'float64']).columns
            numeric_cols = [col for col in numeric_cols if col != target_col]

            for col in numeric_cols:
                plt.figure(figsize=(8, 5))
                sns.scatterplot(x=self.df[col], y=self.df[target_col])
                plt.title(f"{col} vs {target_col}")
                plt.tight_layout()
                file_path = os.path.join(self.save_dir, f"{col}_vs_{target_col}.png")
                plt.savefig(file_path)
                plt.close()

                logging.info(f"Saved scatterplot: {col} vs {target_col}")
        except Exception as e:
            raise CustomException(e, sys)

    def plot_boxplots(self):
        try:
            numeric_cols = self.df.select_dtypes(include=['int64', 'float64']).columns

            for col in numeric_cols:
                plt.figure(figsize=(8, 5))
                sns.boxplot(y=self.df[col])
                plt.title(f"Boxplot of {col}")
                plt.tight_layout()
                file_path = os.path.join(self.save_dir, f"{col}_boxplot.png")
                plt.savefig(file_path)
                plt.close()

                logging.info(f"Saved boxplot for: {col}")

        except Exception as e:
            raise CustomException(e, sys)   