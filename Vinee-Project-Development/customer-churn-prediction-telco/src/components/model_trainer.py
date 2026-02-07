import sys
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from logger.logger import logger
from exception.exception import CustomException
from src.config import PROJECT_ROOT

class ModelTrainer:
    def __init__(self):
        self.model_path = PROJECT_ROOT / "models" / "logistic_regression.pkl"

    def train(self, transformer, X_train, y_train):
        try:
            logger.info("Starting Logistic Regression training")

            model = Pipeline(steps=[
                ("preprocessor", transformer),
                ("classifier", LogisticRegression(
                    max_iter=2000,
                    class_weight="balanced"  # important for churn imbalance
                ))
            ])

            model.fit(X_train, y_train)

            self.model_path.parent.mkdir(exist_ok=True)
            joblib.dump(model, self.model_path)

            logger.info(f"Model training completed and saved at: {self.model_path}")
            return model

        except Exception as e:
            raise CustomException(e, sys)