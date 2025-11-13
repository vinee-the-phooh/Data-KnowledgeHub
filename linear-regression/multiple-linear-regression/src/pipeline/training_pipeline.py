from src.components.data_ingestion import DataIngestion
from src.components.data_visualization import DataVisualization
from src.components.data_preprocessing import DataPreprocessor
from src.components.model_trainer import ModelTrainer
from logger.logger import logging
from exception.exception import CustomException
import sys

def run_training_pipeline():
    try:
        logging.info("======= Training Pipeline Started =======")

        # Data Ingestion
        path = "data/raw/advertising_sales.csv"
        ingestion = DataIngestion(path)
        df = ingestion.initiate_data_ingestion()

        # EDA & Visualization
        viz = DataVisualization(df)
        viz.perform_basic_checks()
        viz.plot_missing_values()
        viz.plot_distributions()
        viz.plot_correlation_heatmap()
        viz.plot_categorical_counts()
        viz.plot_boxplots()
        viz.plot_feature_vs_target(target_col="Units_Sold")     

        # Data Preprocessing
        preprocessor = DataPreprocessor(df, target_col="Units_Sold")
        X_processed, y = preprocessor.initiate_data_preprocessing()

        # Model Training
        trainer = ModelTrainer()
        model, metrics = trainer.train_model(X_processed, y)

        logging.info(f"Training completed successfully with metrics: {metrics}")
        logging.info("======= Training Pipeline Completed Successfully =======")

        # === Model Evaluation using CLEAN data ===
        from src.components.model_evaluation import ModelEvaluation

        evaluator = ModelEvaluation()

        clean_df = preprocessor.df               # CLEANED dataframe
        X_eval = clean_df.drop(columns=["Units_Sold"])
        y_eval = clean_df["Units_Sold"]

        metrics_eval, predictions = evaluator.evaluate_model(X_eval, y_eval)

        logging.info(f"Reloaded model evaluation metrics: {metrics_eval}")

    except Exception as e:
        logging.error("Error occurred during training pipeline execution")
        raise CustomException(e, sys)


if __name__ == "__main__":
    run_training_pipeline()
    print("Pipeline execution completed successfully.")