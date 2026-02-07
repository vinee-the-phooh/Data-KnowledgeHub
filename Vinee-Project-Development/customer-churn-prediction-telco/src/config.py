from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_RAW_DIR = PROJECT_ROOT / "data" / "raw"
RAW_FILE_NAME = "WA_Fn-UseC_-Telco-Customer-Churn.csv"
TARGET_COL = "Churn"