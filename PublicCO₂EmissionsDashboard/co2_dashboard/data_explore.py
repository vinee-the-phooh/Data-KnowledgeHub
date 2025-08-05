import pandas as pd
from core.logger_config import setup_logger
from core.custom_exceptions import AppError

logger = setup_logger("data_explore")

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the dataset from the specified file path.
    """
    try:
        logger.info(f"Load data from: {file_path}")
        df = pd.read_csv(file_path)
        logger.info(f"---Data Loaded Successfully. Rows: {len(df)}, Columns: {len(df.columns)}")
        return df

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise AppError(f"File not found: {file_path}")

    except pd.errors.EmptyDataError:
        logger.error("CSV file is empty.")
        raise AppError("CSV file is empty.")

    except Exception as e:
        logger.error(f"Unexpected error while loading data: {e}")
        raise AppError(f"Error loading data: {e}")

def display_data_info(df: pd.DataFrame):
    """
    Display basic information about the DataFrame.
    """
    try:
        logger.info("---Displaying dataset information---")
        print(f"First 5 rows of the dataset:\n{df.head()}")
        print(f"\nLast 5 rows of the dataset:\n{df.tail()}")
        print(f"\nShape of the dataset: {df.shape}")
        print(f"\nColumns in the dataset:\n{df.columns.tolist()}")
        print(f"\nData Types of each column:\n{df.dtypes}")
        print(f"\nSummary Statistics:\n{df.describe()}")
        logger.info("Dataset information displayed successfully.")

    except Exception as e:
        logger.error(f"Error displaying data info: {e}")
        raise AppError(f"Error displaying data info: {e}")
