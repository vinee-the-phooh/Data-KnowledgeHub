import sys
from sklearn.linear_model import LinearRegression, Ridge, ElasticNet

from logger.logger import logger
from exception.exception import CustomException

class ModelTrainer:
    def train_models(self, X_train, y_train):
        try:
            models = {
                "LinearRegression": LinearRegression(),
                "Ridge": Ridge(alpha=1.0),
                "ElasticNet": ElasticNet(alpha=0.1, l1_ratio=0.5)
            }

            trained_models = {}

            for name, model in models.items():
                model.fit(X_train, y_train)
                trained_models[name] = model
                logger.info(f"{name} trained successfully")

            return trained_models

        except Exception as e:
            raise CustomException(e, sys)