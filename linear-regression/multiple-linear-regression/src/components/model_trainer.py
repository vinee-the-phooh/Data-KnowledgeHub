import os
import sys
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from logger.logger import logging
from exception.exception import CustomException


class ModelTrainer:
    def __init__(self):
        self.models_dir = "models"
        self.reports_dir = "reports"
        os.makedirs(self.models_dir, exist_ok=True)
        os.makedirs(self.reports_dir, exist_ok=True)

    def train_model(self, X, y):
        try:
            logging.info("======= Model Training Started =======")

            #Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            logging.info(f"Train Shape: {X_train.shape}, Test Shape: {X_test.shape}")

            #Train Linear Regression model
            model = LinearRegression()
            model.fit(X_train, y_train)
            logging.info("Linear Regression model training completed.")

            #Predict
            y_pred = model.predict(X_test)

            #Evaluate model
            mae = mean_absolute_error(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            metrics = {"MAE": mae, "MSE": mse, "R2": r2}
            logging.info(f"Model Evaluation Metrics: {metrics}")

            #Save metrics report
            metrics_path = os.path.join(self.reports_dir, "metrics.json")
            pd.Series(metrics).to_json(metrics_path)
            logging.info(f"Metrics saved at {metrics_path}")

            #Save trained model
            model_path = os.path.join(self.models_dir, "linear_regression_model.pkl")
            with open(model_path, "wb") as f:
                pickle.dump(model, f)
            logging.info(f"Trained model saved at {model_path}")

            logging.info("======= Model Training Completed Successfully =======")

            return model, metrics

        except Exception as e:
            logging.error("Error occurred during model training")
            raise CustomException(e, sys)