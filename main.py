import requests

from_currency = str(input("from currency? "))
to_currency = str(input("to currency? "))
ammount = float(input("enter your ammount: "))

api_key = ""

r = requests.get(f"https://openexchangerates.org/api/latest.json?app_id={api_key}")

if r.status_code == 200:
    data = r.json()
    exchange_rate = data["rates"][to_currency] / data["rates"][from_currency]
    converted_amount = ammount * exchange_rate
    intger_ammount = int(converted_amount)
    converted_amount_final = "{:,}".format(intger_ammount)
    print(f"{ammount} {from_currency} is {converted_amount_final} {to_currency}")
else:
    print("Ether the API key is wrong or it is down.")