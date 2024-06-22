from datetime import datetime
import pandas
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv("../../.env")

MY_EMAIL = "ankushinstagram57@gmail.com"
MY_PASSWORD = os.getenv("EMAIL_PASSWORD")

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file_path:
        contents = file_path.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_dict["email"],
            msg=f"Subject:Happy Birthday from Ankush!\n\n{contents}"
        )