from logger.logger import logger
from exception.exception import CustomException
import sys

from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import DataPreprocessing
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

def run_training_pipeline():
    try:
        logger.info("======= Regression Pipeline Started =======")

        df = DataIngestion().load_data()
        X_train, X_test, y_train, y_test = DataPreprocessing().split_and_scale(df)
        models = ModelTrainer().train_models(X_train, y_train)
        ModelEvaluation().evaluate(models, X_test, y_test)

        logger.info("======= Regression Pipeline Completed =======")

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    run_training_pipeline()