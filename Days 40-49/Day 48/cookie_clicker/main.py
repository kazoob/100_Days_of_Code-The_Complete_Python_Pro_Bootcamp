from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

PURCHASE_INTERVAL_SEC = 5
GAME_RUN_MIN = 5


def purchase_upgrades():
    while purchase_next_upgrade():
        time.sleep(0.05)


def purchase_next_upgrade():
    cookies = int(driver.find_element(By.ID, "money").text.replace(",", ""))
    store = get_store()

    print(f"Purchasing upgrade with {cookies} cookies")

    for store_item in store:
        if cookies // store_item["price"] > 0:
            driver.find_element(By.ID, value=store_item["id"]).click()
            print(f"Purchased {store_item["id"].replace("buy", "")} for {store_item["price"]} cookies")
            return True

    print("Not enough cookies to purchase an upgrade")
    return False


def get_store():
    store = []

    store_items = driver.find_elements(by=By.CSS_SELECTOR, value="#store > div")

    for store_item in store_items:
        try:
            store_id = store_item.get_attribute("id").replace(" ", "\\ ")

            price_element = driver.find_element(By.CSS_SELECTOR, value=f"#{store_id} > b")
            item_price = int(price_element.text.split("-")[1].strip().replace(",", ""))

            new_item = {
                "id": store_id,
                "price": item_price,
            }

            store.append(new_item)
        except IndexError:
            pass
        except StaleElementReferenceException:
            return get_store()
        except NoSuchElementException:
            pass
        except Exception as e:
            print(f"Error: {type(e).__name__}")

    store.reverse()

    return store


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

game_end: float = time.time() + GAME_RUN_MIN * 60
purchase_time: float = time.time() + PURCHASE_INTERVAL_SEC

while time.time() < game_end:
    if time.time() >= purchase_time:
        purchase_upgrades()
        print("\n")
        purchase_time = time.time() + PURCHASE_INTERVAL_SEC

    driver.find_element(By.ID, "cookie").click()

print(f"Final score after {GAME_RUN_MIN} minutes: {driver.find_element(By.ID, "cps").text}")

driver.quit()
