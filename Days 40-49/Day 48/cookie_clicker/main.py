from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"
PURCHASE_INTERVAL_SEC = 5  # Interval to purchase upgrades in seconds
PURCHASE_MULTIPLE = False  # Purchase multiple items every purchase interval
GAME_RUN_MIN = 5  # Game run time in minutes


def purchase_upgrades():
    """Purchase available upgrades."""
    # Keep purchasing upgrades if multiple purchases enabled.
    while purchase_next_upgrade() and PURCHASE_MULTIPLE:
        # Delay to allow game to register purchase click
        time.sleep(0.06)


def purchase_next_upgrade() -> bool:
    """Purchase the highest affordable upgrade. Return True if an upgrade was purchased, otherwise return False."""
    # Get cookie value.
    cookies = int(driver.find_element(By.ID, "money").text.replace(",", ""))

    # Get store item names and prices.
    store = get_store()

    print(f"Purchasing upgrade with {cookies} cookies")

    # Go through each store item.
    for store_item in store:
        # Check if enough cookies to purchase one item.
        if cookies // store_item["price"] > 0:
            # Purchase the item.
            driver.find_element(By.ID, value=store_item["id"]).click()

            # Return True to indicate successful purchase.
            print(f"Purchased {store_item["id"].replace("buy", "")} for {store_item["price"]} cookies")
            return True

    # Return False to indicate unsuccessful purchase.
    print("Not enough cookies to purchase an upgrade")
    return False


def get_store() -> list:
    """Return the store items and prices. Prices are ordered from highest to lowest."""
    # Store list.
    store = []

    # Get store element.
    store_items = driver.find_elements(by=By.CSS_SELECTOR, value="#store > div")

    # Go through each store item.
    for store_item in store_items:
        try:
            # Get the store item element class name.
            store_id = store_item.get_attribute("id").replace(" ", "\\ ")

            # Get the store item price.
            price_element = driver.find_element(By.CSS_SELECTOR, value=f"#{store_id} > b")
            item_price = int(price_element.text.split("-")[1].strip().replace(",", ""))

            # Build new store item dict.
            new_item = {
                "id": store_id,
                "price": item_price,
            }

            # Append new store item dict to store list.
            store.append(new_item)
        # Skip over invalid store item.
        except IndexError:
            pass
        # If store changes during processing (usually due to cookie number increasing from buildings and a new
        # option becoming available), get a new store.
        except StaleElementReferenceException:
            return get_store()
        # Skip over invalid store item.
        except NoSuchElementException:
            pass
        # Print any other error to the console.
        except Exception as e:
            print(f"Error: {type(e).__name__}")

    # Order the store prices from highest to lowest.
    store.reverse()

    # Return the store.
    return store


# Set up browser driver.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Set the game end time.
game_end: float = time.time() + GAME_RUN_MIN * 60

# Set the next purchase interval.
purchase_time: float = time.time() + PURCHASE_INTERVAL_SEC

# Continue to run game until game end time.
current_time: float = time.time()
while current_time < game_end:
    # Purchase interval has been reached.
    if current_time >= purchase_time:
        # Purchase items.
        purchase_upgrades()

        print("")

        # Set next purchase interval.
        purchase_time = current_time + PURCHASE_INTERVAL_SEC

        # Display remaining game time.
        minutes_remaining: int = round((game_end - current_time) // 60)
        seconds_remaining: int = round((game_end - current_time) % 60)
        print(f"Game time remaining: {minutes_remaining} minutes, {seconds_remaining} seconds\n")

    # Click cookie every loop.
    driver.find_element(By.ID, "cookie").click()

    # Update current time.
    current_time = time.time()

# Display end score.
print(f"Final score after {GAME_RUN_MIN} minutes: {driver.find_element(By.ID, "cps").text}")

# Quit browser.
driver.quit()
