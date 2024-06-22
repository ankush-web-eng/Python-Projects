from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

name = driver.find_element(By.XPATH, value='//*[@id="about"]/a')
event_dates = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
# print(event_names)
# for i in event_dates:
#     print(i.text)
# for i in event_names:
#     print(i.text)

events = {}

for n in range(len(event_names)):
    events[n] = {
        'date': event_dates[n].text,
        'title': event_names[n].text
    }
print(events)

driver.quit()