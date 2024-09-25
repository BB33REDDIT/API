from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/pizza-news')
def get_pizza_news():
    url = 'https://newsdata.io/api/1/news?apikey=544864f49d63cm81c7478f2730@f5d3ccare&q=pizza'
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000)
