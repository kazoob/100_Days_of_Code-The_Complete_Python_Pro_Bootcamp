from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_num_element = driver.find_element(By.CSS_SELECTOR, value="#articlecount a").text
article_num = int(article_num_element.replace(",",""))
print(article_num)

# driver.close()
driver.quit()
