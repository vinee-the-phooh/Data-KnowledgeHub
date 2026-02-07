import pandas as pd
from src.config import DATA_RAW_DIR, RAW_FILE_NAME

class DataIngestion:
    def __init__(self):
        self.file_path = DATA_RAW_DIR / RAW_FILE_NAME

    def load_data(self) -> pd.DataFrame:
        if not self.file_path.exists():
            raise FileNotFoundError(f"Dataset not found at: {self.file_path}")
        df = pd.read_csv(self.file_path)
        return df