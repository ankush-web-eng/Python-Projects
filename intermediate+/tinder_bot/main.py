from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv("../../.env")

URL = "https://tinder.com/"
EMAIL = os.getenv("FB_EMAIL")
PASSWORD = os.getenv("FB_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(URL)

sleep(2)
cookie = driver.find_element(By.XPATH, value='//*[@id="s1524772468"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookie.click()

sleep(2)
sign_in = driver.find_element(By.XPATH, value='//*[@id="s1524772468"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
sign_in.click()

sleep(2)
more_options = driver.find_element(By.XPATH, value='//*[@id="s1746112904"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button')
more_options.click()

sleep(2)
facebook = driver.find_element(By.XPATH, value='//*[@id="s1746112904"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
facebook.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

sleep(2)
email = driver.find_element(By.XPATH,value='//*[@id="email"]')
password = driver.find_element(By.XPATH,value='//*[@id="pass"]')
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

sleep(5)
allow_location_button = driver.find_element(By.XPATH,value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH,value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element(By.XPATH,value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()


for n in range(100):

    sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH,value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR,value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()