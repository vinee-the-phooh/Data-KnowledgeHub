import sys
import json
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

from logger.logger import logger
from exception.exception import CustomException
from src.config import PROJECT_ROOT

class ModelEvaluation:
    def evaluate(self, models, X_test, y_test):
        try:
            results = {}

            for name, model in models.items():
                y_pred = model.predict(X_test)

                rmse = np.sqrt(mean_squared_error(y_test, y_pred))
                r2 = r2_score(y_test, y_pred)

                results[name] = {
                    "RMSE": rmse,
                    "R2": r2
                }

                logger.info(f"{name} → RMSE: {rmse:.4f}, R2: {r2:.4f}")

            metrics_path = PROJECT_ROOT / "reports" / "metrics" / "metrics.json"
            metrics_path.parent.mkdir(parents=True, exist_ok=True)

            with open(metrics_path, "w") as f:
                json.dump(results, f, indent=4)

            return results

        except Exception as e:
            raise CustomException(e, sys)