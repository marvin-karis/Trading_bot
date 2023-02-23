import requests

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"time_period":"21","interval":"5min","series_type":"close","function":"SMA","symbol":"GBPUSD","datatype":"json"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "###########################"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
