import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def transaction_convert_currency(transaction: dict) -> float:

    operation_amount = transaction.get("operationAmount", {})
    amount_str = operation_amount.get("amount")
    currency_dict = operation_amount.get("currency", {})
    currency_code = currency_dict.get("code")
    amount = 0.0
    try:
        amount = float(amount_str)
    except ValueError:
        return amount
    if currency_code == "RUB":
        return amount
    elif currency_code in ["USD", "EUR"]:
        try:
            exchange_url = "https://api.apilayer.com/exchangerates_data/latest"
            headers = {"apikey": API_KEY} if API_KEY else {}
            params = {"base": currency_code, "symbols": "RUB"}

            response = requests.get(exchange_url, headers=headers, params=params, timeout=10)
            if response.status_code != 200:
                return amount
            else:
                response_data = response.json()
                print(response_data)
                rub_rate = response_data.get("rates", {}).get("RUB")
                if rub_rate is None:
                    return 0.0
                return float(round(amount * rub_rate, 2))
        except (requests.RequestException, KeyError, ValueError):
            return amount
    return amount


if __name__ == "__main__":
    print(
        transaction_convert_currency(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
            }
        )
    )
