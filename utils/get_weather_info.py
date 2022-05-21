import requests
from config import OP_API_KEY


latitude = 54.775
longitude = 56.0375


def get_weather(lat: float, lon: float, api_key: str) -> dict:
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=ru&APPID={api_key}'
    r = requests.get(url)
    return r.json()


def get_weather_info() -> str:
    res = get_weather(lat=latitude, lon=longitude, api_key=OP_API_KEY)
    res = f"Уфа, {res['weather'][0]['description']},\n\n" \
          f"температура: {round(res['main']['temp'])} `C, ощущается как: {round(res['main']['feels_like'])} `C\n\n" \
          f"влажность: {res['main']['humidity']}%"
    return res