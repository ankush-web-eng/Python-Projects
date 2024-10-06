from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_gold_price():
    headers = {
        'Host': 'www.livemint.com',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.google.com/',
        'accept-language': 'en-US,en;q=0.9',
        'priority': 'u=0, i',
    }

    response = requests.get('https://www.livemint.com/gold-prices', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tag = soup.select_one('script#__NEXT_DATA__').text
    jsn = json.loads(tag)
    city_list = jsn['props']['pageProps']['goldMetroCitiesData']

    for city in city_list:
        if city['city'].lower() == 'delhi':
            price = int(city['price24Cr']) / 10
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return jsonify({'city': 'Delhi', 'price': price, 'timestamp': timestamp})

    return jsonify({'error': 'City not found'}), 404
