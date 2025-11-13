import os
import sys
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from logger.logger import logging
from exception.exception import CustomException


class ModelEvaluation:
    def __init__(self):
        self.model_path = os.path.join("models", "linear_regression_model.pkl")
        self.preprocessor_path = os.path.join("models", "preprocessor.pkl")

    def load_objects(self):
        try:
            logging.info("======= Model & Preprocessor Loading Started =======")

            if not os.path.exists(self.model_path):
                raise CustomException(f"Model file not found at {self.model_path}", sys)

            if not os.path.exists(self.preprocessor_path):
                raise CustomException(f"Preprocessor file not found at {self.preprocessor_path}", sys)

            with open(self.model_path, "rb") as model_file:
                model = pickle.load(model_file)

            with open(self.preprocessor_path, "rb") as prep_file:
                preprocessor = pickle.load(prep_file)

            logging.info("Model and preprocessor loaded successfully.")
            return model, preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def evaluate_model(self, X, y):
        try:
            logging.info("======= Model Evaluation Started =======")

            model, preprocessor = self.load_objects()

            # Ensure features are transformed using the same preprocessor
            X_processed = preprocessor.transform(X)
            y_pred = model.predict(X_processed)

            mae = mean_absolute_error(y, y_pred)
            mse = mean_squared_error(y, y_pred)
            r2 = r2_score(y, y_pred)

            metrics = {"MAE": mae, "MSE": mse, "R2": r2}
            logging.info(f"Evaluation Metrics after reload: {metrics}")

            logging.info("======= Model Evaluation Completed =======")
            return metrics, y_pred

        except Exception as e:
            logging.error("Error during model evaluation")
            raise CustomException(e, sys)