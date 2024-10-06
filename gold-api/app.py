from flask import Flask, jsonify
import requests
from datetime import datetime
from flask import Flask, jsonify
from datetime import datetime
import json
from dotenv import load_dotenv
import os


# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
load_dotenv()


app = Flask(__name__)

def make_gapi_request():
    api_key = os.getenv("GOLD_API_KEY")
    symbol = "XAU"
    curr = "INR"
    date = ""

    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        response_str = response.text
        response_data = json.loads(response_str)
        price_gram_24k = response_data.get("price_gram_24k")
        print("Price per gram of 24K gold:", price_gram_24k)
        return price_gram_24k
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))
        return None


@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Gold Price API"

@app.route('/get-gold-price', methods=['GET'])
def gold_price_api():
    price = make_gapi_request()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if price:
        return jsonify({
            "gold_price": price,
            "timestamp": timestamp
        })
    else:
        return jsonify({
            "error": "Unable to fetch the gold price",
            "timestamp": timestamp
        }), 500

if __name__ == '__main__':
    app.run(debug=True)

# def get_gold_price():
#     options = Options()
#     options.page_load_strategy = 'normal'
#     options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option('useAutomationExtension', False)
#     options.add_argument('--disable-blink-features=AutomationControlled')
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--disable-infobars")
#     options.add_argument("--disable-extensions")
#     options.add_argument("--disable-popup-blocking")
#     options.add_argument('--ignore-certificate-errors-spki-list')
#     options.add_argument('--ignore-ssl-errors')
#     options.add_argument("--headless=new")

#     driver = webdriver.Chrome(options=options)

#     try:
#         url = 'https://www.goodreturns.in/gold-rates/'
#         driver.get(url)
#         element = driver.find_element(By.XPATH, '//*[@id="moneyweb-leftPanel"]/setion/div/div[2]/div[2]/p')
#         gold_price = element.text
#     except Exception as e:
#         gold_price = None
#         print(f"Error: {e}")
#     finally:
#         driver.quit()

#     return gold_price