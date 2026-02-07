from logger.logger import logger
from exception.exception import CustomException
import sys
from src.components.data_ingestion import DataIngestion
from src.config import TARGET_COL
from src.components.data_preprocessing import DataPreprocessing
from src.components.feature_engineering import FeatureEngineering
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation


def run_training_pipeline():
    try:
        logger.info("======= Training Pipeline Started =======")

        ingestion = DataIngestion()
        df = ingestion.load_data()

        logger.info(f"Data loaded successfully. Shape: {df.shape}")
        logger.info(f"Columns: {list(df.columns)}")

        if TARGET_COL in df.columns:
            logger.info(f"Target '{TARGET_COL}' distribution:\n{df[TARGET_COL].value_counts(dropna=False)}")
        else:
            logger.warning(f"Target column '{TARGET_COL}' not found!")

        logger.info("======= Training Pipeline Completed (Ingestion step) =======")

        preprocessor = DataPreprocessing(test_size=0.2, random_state=42)
        df_clean = preprocessor.clean_data(df)
        logger.info(f"Cleaned data shape: {df_clean.shape}")
        # Check missing values (top 5)
        logger.info(f"Top missing values:\n{df_clean.isna().sum().sort_values(ascending=False).head(5)}")
        X_train, X_test, y_train, y_test = preprocessor.split_data(df_clean)

        fe = FeatureEngineering()
        transformer = fe.build_transformer(X_train)

        # Fit transformer on train and transform both
        X_train_tr = transformer.fit_transform(X_train)
        X_test_tr = transformer.transform(X_test)

        logger.info(f"Transformed train shape: {X_train_tr.shape}")
        logger.info(f"Transformed test shape: {X_test_tr.shape}")

        trainer = ModelTrainer()
        model = trainer.train(transformer, X_train, y_train)

        evaluator = ModelEvaluation()
        metrics = evaluator.evaluate(model, X_test, y_test)
    
    except Exception as e:
        logger.error("Error occurred during training pipeline execution")
        raise CustomException(e, sys)


if __name__ == "__main__":
    run_training_pipeline()
    print("Pipeline execution completed successfully.")