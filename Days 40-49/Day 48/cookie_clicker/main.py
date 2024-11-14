from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from threading import Timer

PURCHASE_INTERVAL = 5


def purchase():
    print("Purchasing")
    start_purchase_timer()


def start_purchase_timer():
    purchase_timer = Timer(PURCHASE_INTERVAL, purchase)
    purchase_timer.start()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

start_purchase_timer()

while True:
    cookie.click()

# driver.close()
driver.quit()
