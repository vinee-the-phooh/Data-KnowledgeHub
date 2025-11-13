from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import DataPreprocessing
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

if __name__ == "__main__":
    RAW_PATH = "data/raw/simple_linear_regression_dataset.csv"
    PROCESSED_PATH = "data/processed/clean_data.csv"

    ingestion = DataIngestion(raw_data_path=RAW_PATH, processed_data_path=PROCESSED_PATH)
    df = ingestion.initiate_data_ingestion()
    print(df.head())

    PRE_PROCESSED_PATH = "data/processed/clean_data.csv"
    OUTPUT_PATH = "data/processed/final_clean_data.csv"

    preprocess = DataPreprocessing(PRE_PROCESSED_PATH, OUTPUT_PATH)
    df_clean = preprocess.initiate_data_preprocessing()
    print(df_clean.head())

    CLEAN_DATA = "data/processed/final_clean_data.csv"
    MODEL_PATH = "artifacts/simple_linear_regression_model.pkl"

    trainer = ModelTrainer(CLEAN_DATA, MODEL_PATH)
    training_output = trainer.initiate_model_training()
    print("Model Evaluation Metrics:", training_output)

    CLEAN_DATA = "data/processed/final_clean_data.csv"
    MODEL_PATH = "artifacts/simple_linear_regression_model.pkl"
    METRICS_PATH = "artifacts/metrics.json"

    # Evaluate (using training output directly)
    evaluator = ModelEvaluation(training_output, METRICS_PATH)
    metrics = evaluator.initiate_model_evaluation()
    print(metrics)