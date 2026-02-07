import sys
import json
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    roc_curve
)

from logger.logger import logger
from exception.exception import CustomException
from src.config import PROJECT_ROOT

class ModelEvaluation:
    def __init__(self):
        self.metrics_path = PROJECT_ROOT / "reports" / "metrics" / "metrics.json"
        self.figures_path = PROJECT_ROOT / "reports" / "figures"
        self.figures_path.mkdir(parents=True, exist_ok=True)

    def evaluate(self, model, X_test, y_test):
        try:
            logger.info("Starting model evaluation")

            y_pred = model.predict(X_test)
            y_proba = model.predict_proba(X_test)[:, 1]

            metrics = {
                "accuracy": accuracy_score(y_test, y_pred),
                "precision": precision_score(y_test, y_pred),
                "recall": recall_score(y_test, y_pred),
                "f1_score": f1_score(y_test, y_pred),
                "roc_auc": roc_auc_score(y_test, y_proba),
                "confusion_matrix": confusion_matrix(y_test, y_pred).tolist()
            }

            logger.info(f"Evaluation Metrics: {metrics}")

            self._save_metrics(metrics)
            self._save_roc_curve(y_test, y_proba)

            return metrics

        except Exception as e:
            raise CustomException(e, sys)

    def _save_metrics(self, metrics: dict):
        self.metrics_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.metrics_path, "w") as f:
            json.dump(metrics, f, indent=4)

        logger.info(f"Metrics saved to {self.metrics_path}")

    def _save_roc_curve(self, y_test, y_proba):
        fpr, tpr, _ = roc_curve(y_test, y_proba)

        plt.figure()
        plt.plot(fpr, tpr, label="Logistic Regression")
        plt.plot([0, 1], [0, 1], linestyle="--")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("ROC Curve")
        plt.legend()

        path = self.figures_path / "roc_curve.png"
        plt.savefig(path, bbox_inches="tight")
        plt.close()

        logger.info(f"ROC curve saved at {path}")