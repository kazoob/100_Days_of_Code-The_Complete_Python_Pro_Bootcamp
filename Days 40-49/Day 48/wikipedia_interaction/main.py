from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Get article count
article_num_element = driver.find_element(By.CSS_SELECTOR, value="#articlecount a").text
article_num = int(article_num_element.replace(",",""))
print(article_num)

# Click content portals link
content_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portals.click()

# Search for "Python"
search_field = driver.find_element(By.NAME, value="search")
search_field.send_keys("Python", Keys.ENTER)

# driver.close()
# driver.quit()
