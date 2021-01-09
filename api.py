import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"callback":"test","id":"2172797","units":"%22imperial%22","mode":"xml%2C html","q":"SanJuan%2Cpr"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "0a8ae5c168msh87f0c5550832eabp1bd257jsn05f84d1dd46c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)