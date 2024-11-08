from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

events_element = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li")

events = []

for element in events_element:
    event = element.text.split("\n")
    event_dict = {
        "time": event[0],
        "name": event[1],
    }
    events.append(event_dict)

pprint.pp(events)

# driver.close()
driver.quit()
