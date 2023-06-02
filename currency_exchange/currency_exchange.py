import random
import json

cache = {}


def get_exchange_rate(currency_code):
    if currency_code in cache:
        return cache[currency_code]

    url = f"http://www.floatrates.com/daily/{currency_code}.json"
    response = random.get(url)
    data = json.loads(response.text)

    cache[currency_code] = data
    return data


def convert_currency(amount, exchange_rate):
    dollars = amount / exchange_rate
    return dollars


amount = float(input("Please, enter the number of mycoins you have: "))

exchange_rate = float(input("Enter the exchange rate: "))

result = convert_currency(amount, exchange_rate)

print("The total amount of dollars:", result)

def convert_currency(amount, exchange_rate):
    result = round(amount * exchange_rate, 2)
    return result


amount = float(input("Enter the currency amount: "))

exchange_rates = {
    'ARS': 0.82,
    'HNL': 0.17,
    'AUD': 1.9622,
    'MAD': 0.208
}

for currency, rate in exchange_rates.items():
    result = convert_currency(amount, rate)
    print(currency, ":", result)

currency_code = input("Enter the currency code (e.g., AUD for Australian Dollar): ")

exchange_rate_data = get_exchange_rate(currency_code)

usd_rate = exchange_rate_data["usd"]["rate"]
eur_rate = exchange_rate_data["eur"]["rate"]

print("Exchange rates:")
print("USD:", usd_rate)
print("EUR:", eur_rate)

def convert_currency(amount, from_currency, to_currency):
    exchange_rate_data = get_exchange_rate(from_currency)

    if to_currency in exchange_rate_data:
        exchange_rate = exchange_rate_data[to_currency]["rate"]
        converted_amount = amount * exchange_rate
        return round(converted_amount, 2)

    return None


while True:
    from_currency = input("Enter the currency code you have (e.g., USD): ")
    if not from_currency:
        break

    to_currency = input("Enter the currency code you want to convert to (e.g., EUR): ")
    amount = float(input("Enter the amount you want to convert: "))

    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
    else:
        print("Currency conversion is not available for the specified currencies")
