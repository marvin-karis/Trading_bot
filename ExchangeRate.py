import requests

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"to_currency":"TZS","function":"CURRENCY_EXCHANGE_RATE","from_currency":"USD"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "########################"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
