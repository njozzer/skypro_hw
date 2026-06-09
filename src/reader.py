import csv
import pandas as pd

def csv_read(file_path: str) -> list[dict]:
    with open(file_path) as file:
        reader = csv.DictReader(file)

def excel_read(file_path: str) -> list[dict]:
    pass


if __name__ == "__main__":
    pass