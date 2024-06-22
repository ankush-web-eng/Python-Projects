import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from dotenv import load_dotenv

load_dotenv("../../.env")

my_deal = "https://www.amazon.in/gp/product/0141988517/ref=ox_sc_saved_image_2?smid=A1WYWER0W24N8S&psc=1"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"
}
EMAIL = "ankushinstagram57@gmail.com"
PASSWORD = os.getenv("EMAIL_PASSWORD")

response = requests.get(url=my_deal, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

content = f"The Price of book '12 Rules for Life' by JORDAN PETERSON has changed to Rupees.{price_without_currency}"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(EMAIL,PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs="ankushsingh57d@gmail.com",
        msg=f"Subject:Sent by Ankush!\n\n{content}"
    )