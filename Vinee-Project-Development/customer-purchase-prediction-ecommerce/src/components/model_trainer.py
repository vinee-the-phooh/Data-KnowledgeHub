import sys
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from logger.logger import logger
from exception.exception import CustomException
from src.config import PROJECT_ROOT

class ModelTrainer:
    def train(self, transformer, X_train, y_train):
        try:
            model = Pipeline(
                steps=[
                    ("preprocessor", transformer),
                    ("classifier", LogisticRegression(
                        max_iter=2000,
                        class_weight="balanced"
                    ))
                ]
            )

            model.fit(X_train, y_train)

            model_path = PROJECT_ROOT / "models" / "logistic_regression.pkl"
            model_path.parent.mkdir(exist_ok=True)
            joblib.dump(model, model_path)

            logger.info(f"Model trained and saved at {model_path}")

            return model

        except Exception as e:
            raise CustomException(e, sys)