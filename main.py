from pathlib import Path
from typing import Any, Dict, List, Optional


DATA_DIR: Path = Path(__file__).resolve().parent / "data"
FILE_PATHS: Dict[str, str] = {
    "json": str(DATA_DIR / "operations.json"),
    "csv": str(DATA_DIR / "transactions.csv"),
    "xlsx": str(DATA_DIR / "transactions_excel.xlsx"),
}

if __name__ == "__main__":
    pass