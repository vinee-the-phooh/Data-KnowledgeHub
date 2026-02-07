from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
TARGET_COL = "MedHouseVal"

RANDOM_STATE = 42
TEST_SIZE = 0.2