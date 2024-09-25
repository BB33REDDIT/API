import requests

def get_weather(city, api_key, units):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    request = requests.get(url)
    content = request.json()
    print(content)

get_weather("kannur","4a478ed6be1c20c20ff21c82ff989686",'standard')