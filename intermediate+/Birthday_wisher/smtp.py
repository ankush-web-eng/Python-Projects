# import smtplib

# my_email = "ankushinstagram57@gmail.com"
# password = ""

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()                                   # Make Connection Secure
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="ankushsingh57@yahoo.com",
#         msg="Subject:Hello, It's me Ankush!\n\nThis is the email for testing!!"
#     )

# import datetime as dt

# now = dt.datetime.now()
# day = now.day
# month = now.month
# if month == 3:
#     month = "March"
# print(f"It's {day} of {month}!! ")