import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.logger import logging
from src.exception import CustomException

"""
Step 1: Load dataset
Step 2: Data overview
Step 3: Visualization
Step 4: Handle missing values
Step 5: Remove duplicates
Step 6: Save cleaned data
"""

class DataPreprocessing:
    def __init__(self, processed_data_path: str, output_clean_path: str):
        self.processed_data_path = processed_data_path
        self.output_clean_path = output_clean_path

    def initiate_data_preprocessing(self):
        logging.info("==== Data Preprocessing started ====")

        try:
            df = pd.read_csv(self.processed_data_path)
            logging.info(f"Loaded dataset from {self.processed_data_path} with shape {df.shape}")

            logging.info(f"Columns: {df.columns.tolist()}")
            logging.info(f"Missing values:\n{df.isnull().sum().to_dict()}")
            logging.info(f"Duplicate rows: {df.duplicated().sum()}")

            plt.figure(figsize=(6,4))
            sns.scatterplot(data=df, x='hours_studied', y='score')
            plt.title("Hours Studied vs Score")
            plt.savefig("artifacts/scatter_hours_score.png")
            plt.close()

            plt.figure(figsize=(5,3))
            sns.heatmap(df.corr(), annot=True, cmap="Blues")
            plt.title("Feature Correlation")
            plt.savefig("artifacts/correlation_heatmap.png")
            plt.close()
            logging.info("Exploratory plots saved to artifacts/")

           
            df["hours_studied"].fillna(df["hours_studied"].mean(), inplace=True)
            df["score"].fillna(df["score"].mean(), inplace=True)
            logging.info("Missing values imputed with column mean.")

            
            before = df.shape[0]
            df.drop_duplicates(inplace=True)
            after = df.shape[0]
            logging.info(f"Removed {before - after} duplicate rows.")

            
            os.makedirs(os.path.dirname(self.output_clean_path), exist_ok=True)
            df.to_csv(self.output_clean_path, index=False)
            logging.info(f"Final cleaned dataset saved to {self.output_clean_path}")

            logging.info("==== Data Preprocessing completed successfully ====")
            return df

        except Exception as e:
            logging.error("Error during data preprocessing.")
            raise CustomException(e)