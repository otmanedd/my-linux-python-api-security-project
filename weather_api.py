import requests

API_KEY = "dein_api_schlüssel"
CITY = "Berlin"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    print(f"Wetter in {CITY}: {data['weather'][0]['description']}, {data['main']['temp']}°C")
else:
    print("Fehler beim Abrufen der Wetterdaten.")
