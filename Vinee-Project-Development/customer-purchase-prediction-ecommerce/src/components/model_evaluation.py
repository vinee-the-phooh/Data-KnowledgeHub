import sys
import json
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score, confusion_matrix, roc_curve

from logger.logger import logger
from exception.exception import CustomException
from src.config import PROJECT_ROOT

class ModelEvaluation:
    def evaluate(self, model, X_test, y_test):
        try:
            y_pred = model.predict(X_test)
            y_proba = model.predict_proba(X_test)[:, 1]

            roc_auc = roc_auc_score(y_test, y_proba)
            cm = confusion_matrix(y_test, y_pred)

            metrics = {
                "roc_auc": roc_auc,
                "confusion_matrix": cm.tolist()
            }

            logger.info(f"ROC-AUC: {roc_auc}")
            logger.info(f"Confusion Matrix:\n{cm}")

            # Save metrics
            metrics_path = PROJECT_ROOT / "reports" / "metrics" / "metrics.json"
            metrics_path.parent.mkdir(parents=True, exist_ok=True)
            with open(metrics_path, "w") as f:
                json.dump(metrics, f, indent=4)

            # Save ROC curve
            fpr, tpr, _ = roc_curve(y_test, y_proba)
            plt.figure()
            plt.plot(fpr, tpr, label=f"ROC-AUC = {roc_auc:.3f}")
            plt.plot([0, 1], [0, 1], linestyle="--")
            plt.xlabel("False Positive Rate")
            plt.ylabel("True Positive Rate")
            plt.title("ROC Curve")
            plt.legend()

            fig_path = PROJECT_ROOT / "reports" / "figures" / "roc_curve.png"
            fig_path.parent.mkdir(parents=True, exist_ok=True)
            plt.savefig(fig_path, bbox_inches="tight")
            plt.close()

            logger.info(f"ROC curve saved at {fig_path}")

            return metrics

        except Exception as e:
            raise CustomException(e, sys)