from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from os import getenv
from dotenv import  load_dotenv
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv("../../.env")

EMAIL = getenv("INSTA_ID")
PASSWORD = getenv("INSTA_PASSWORD")
URL = "https://www.instagram.com/"
related_id = "the.kaizenist"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstaFollower():
    def __init__(self, chrome_path):
        self.driver = webdriver.Chrome(chrome_path)

    def login(self):
        self.driver.get(URL)

        sleep(2)
        email = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')

        email.send_keys(EMAIL)
        password.send_keys(PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

        sleep(2)
        # save_login_info = self.driver.find_elements(By.XPATH, value="// button[contains(text(), 'Not Now')]")
        
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='Fifk5']")))

        notification_div = self.driver.find_element(By.XPATH, value="//div[@class='Fifk5']")
        notification_div.click()
    def find_followers(self):
        pass
    def follow(self):
        pass

bot = InstaFollower(chrome_options)
bot.login()

