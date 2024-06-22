from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from time import sleep
import os

load_dotenv("../../.env")
URL = "https://www.linkedin.com/jobs"
ID = os.getenv("LINKEDIN_ID")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(URL)

# Login to LinkedIn
user = driver.find_element(By.XPATH, value='//*[@id="session_key"]')
passwd = driver.find_element(By.XPATH, value='//*[@id="session_password"]')
btn = driver.find_element(By.XPATH,value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')

sleep(2)
user.send_keys(ID)
passwd.send_keys(PASSWORD)
btn.click()

sleep(5) # Wait for page loading
print('Login Successful!')

driver.quit()