import csv

import pandas as pd


def csv_read(file_path: str) -> list[dict]:
    """
    Считывает данные из csv файла
    :param file_path: название файла
    :return: список транзакций
    """
    data_list = []
    if not isinstance(file_path, str):
        return data_list
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            data_list.append(row)
        return data_list


def excel_read(file_path: str) -> list[dict]:
    """
    Считывает данные из excel файла
    :param file_path: название файла
    :return: список транзакций
    """
    data_list = []
    if not isinstance(file_path, str):
        return data_list
    reader = pd.read_excel(file_path)
    for index, row in reader.iterrows():
        data_list.append(dict(row))
    return data_list


if __name__ == "__main__":
    """print(csv_read("data/transactions.csv"))"""
    print(excel_read("data/transactions_excel.xlsx"))
