from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from os import getenv
from dotenv import  load_dotenv
from time import sleep


load_dotenv("../../.env")

EMAIL = getenv("INSTA_ID")
PASSWORD = getenv("INSTA_PASSWORD")
URL = "https://www.instagram.com/"
SIMILAR_ACCOUNT = "the.kaizenist"

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

        
        sleep(4.3)
        # save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        # if save_login_prompt:
        #     save_login_prompt.click()

        # sleep(3.7)
        # notifications_prompt = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        # if notifications_prompt:
        #     notifications_prompt.click()

        
    def find_followers(self):
        sleep(4)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        sleep(4.2)
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):

            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            button.click()
            sleep(1.1)


bot = InstaFollower(chrome_options)
bot.login()
bot.find_followers()
bot.follow()




# In this case we're executing some Javascript, that's what the execute_script() method does.
# The method can accept the script as well as an HTML element.
# The modal in this case, becomes the arguments[0] in the script.
# Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"