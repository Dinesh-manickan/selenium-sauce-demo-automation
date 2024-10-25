from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
from utils.data_handler import save_json


SAUCE_DEMO_URL = "https://www.saucedemo.com/"


def load_credentials(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading credentials: {e}")
        return None


def login(driver, username, password):
    driver.get(SAUCE_DEMO_URL)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url, "Login failed"


def main():
    credentials = load_credentials('app/config.json')
    if credentials is None:
        return

    username = credentials['user_credentials']['username']
    password = credentials['user_credentials']['password']

    driver = webdriver.Chrome()
    try:
        # Login to the website
        login(driver, username, password)

        products = {}
        eles = driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product in eles:
            title = product.find_element(
                By.CLASS_NAME, 'inventory_item_name').text
            description = product.find_element(
                By.CLASS_NAME, 'inventory_item_desc').text
            price = product.find_element(
                By.CLASS_NAME, 'inventory_item_price').text

            products[title] = {
                "description": description,
                "price": price
            }

        # Save Json file
        save_json('data/products.json', products)
        print("Data successfully saved to data/products.json")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    main()
