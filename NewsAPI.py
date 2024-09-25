import requests

def get_news():
    url = f"https://newsapi.org/v1/latest?apikey=b666e55a51b94fae89e652b38b81cb89"
    request = requests.get(url)
    content = request.json()
    print(content)

get_news()