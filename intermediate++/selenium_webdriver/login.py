from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
URL = "http://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

fname  = driver.find_element(By.NAME, value="fName")
lname  = driver.find_element(By.NAME, value="lName")
email  = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CSS_SELECTOR, "form button")

fname.send_keys("Ankush")
lname.send_keys("Singh")
email.send_keys("deshwalankush23@gmail.com")
button.click()
