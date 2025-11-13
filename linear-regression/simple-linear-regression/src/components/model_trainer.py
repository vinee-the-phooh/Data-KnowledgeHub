import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from src.logger import logging
from src.exception import CustomException

"""
Step 1: Load dataset
Step 2: Split features/target
Step 3: Train model
Step 4: Evaluate
Step 5: Save model artifact
Return metrics for downstream pipeline
"""


class ModelTrainer:
    def __init__(self, clean_data_path: str, model_save_path: str):
        self.clean_data_path = clean_data_path
        self.model_save_path = model_save_path

    def initiate_model_training(self):
        logging.info("==== Model Training process started ====")
        try:
            
            df = pd.read_csv(self.clean_data_path)
            logging.info(f"Loaded cleaned dataset: {self.clean_data_path} Shape : {df.shape}")

            
            X = df[["hours_studied"]]
            y = df["score"]
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            logging.info(f"Train / Test split : {X_train.shape} , {X_test.shape}")

            
            model = LinearRegression()
            model.fit(X_train, y_train)
            logging.info("Model training completed successfully.")

            
            y_pred = model.predict(X_test)
            mae = mean_absolute_error(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            logging.info(f"MAE: {mae:.2f}")
            logging.info(f"MSE: {mse:.2f}")
            logging.info(f"R² : {r2:.2f}")

           
            os.makedirs(os.path.dirname(self.model_save_path), exist_ok=True)
            with open(self.model_save_path, "wb") as f:
                pickle.dump(model, f)
            logging.info(f"Trained model saved to {self.model_save_path}")

            logging.info("==== Model Training process completed successfully ====")

            
            return {
                        "MAE": mae,
                        "MSE": mse,
                        "R2": r2,
                        "model_path": self.model_save_path,
                        "X_test": X_test.to_dict(),
                        "y_test": y_test.to_list(),
                        "y_pred": y_pred.tolist()
                    }

        except Exception as e:
            logging.error("Error during model training.")
            raise CustomException(e)