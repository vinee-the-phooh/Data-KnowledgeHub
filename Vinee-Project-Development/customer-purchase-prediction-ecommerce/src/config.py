from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_RAW_DIR = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

RAW_FILE_NAME = "ecommerce.csv"
TARGET_COL = "purchase"   # we will confirm this in logs

RANDOM_STATE = 42
TEST_SIZE = 0.2