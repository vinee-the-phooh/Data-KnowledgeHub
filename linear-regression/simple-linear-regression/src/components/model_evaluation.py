import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src.logger import logging
from src.exception import CustomException

"""
Step 1: Extract from training output
Step 2: Visualizations
Step 3: Save metrics JSON
"""

class ModelEvaluation:
    def __init__(self, training_output: dict, metrics_save_path: str):
        self.training_output = training_output
        self.metrics_save_path = metrics_save_path

    def initiate_model_evaluation(self):
        logging.info("==== Model Evaluation started ====")
        try:
            
            metrics = {
                "MAE": round(self.training_output["MAE"], 2),
                "MSE": round(self.training_output["MSE"], 2),
                "R2": round(self.training_output["R2"], 3)
            }
            logging.info(f"Reusing metrics from training: {metrics}")

           
            y_test = pd.Series(self.training_output["y_test"])
            y_pred = pd.Series(self.training_output["y_pred"])

            plt.figure(figsize=(6, 4))
            sns.scatterplot(x=y_test, y=y_pred)

            # Add reference diagonal line
            min_val = min(y_test.min(), y_pred.min())
            max_val = max(y_test.max(), y_pred.max())
            plt.plot([min_val, max_val], [min_val, max_val], "r--", linewidth=2)

            plt.xlabel("Actual Scores")
            plt.ylabel("Predicted Scores")
            plt.title("Predicted vs Actual Scores")
            plt.savefig("artifacts/predicted_vs_actual.png")
            plt.close()

            residuals = y_test - y_pred
            sns.histplot(residuals, kde=True, bins=10)
            plt.title("Residual Distribution")
            plt.xlabel("Residuals")
            plt.savefig("artifacts/residual_distribution.png")
            plt.close()

            
            with open(self.metrics_save_path, "w") as f:
                json.dump(metrics, f, indent=4)
            logging.info(f"Metrics saved to {self.metrics_save_path}")

            logging.info("==== Model Evaluation completed successfully ====")
            return metrics

        except Exception as e:
            logging.error("Error during model evaluation.")
            raise CustomException(e)