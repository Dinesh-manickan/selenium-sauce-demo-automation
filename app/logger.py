from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
import os

config_path = os.path.join(os.path.dirname(__file__), 'config.json')

with open(config_path, 'r') as creds_file:
    credentials = json.load(creds_file)

login_results = []

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.saucedemo.com/")

for username, password in credentials['users'].items():
    try:
        elem = driver.find_element(By.NAME, "user-name")
        elem.clear()
        elem.send_keys(username)
        elem = driver.find_element(By.NAME, "password")
        elem.clear()
        elem.send_keys(password)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)

        time.sleep(2)

        try:
            error_element = driver.find_element(
                By.CLASS_NAME, "error-message-container")
            error_message = error_element.text
            login_results.append(
                f"Login failed for user: {username} - Reason: {error_message}")
        except Exception:
            login_results.append(f"Login successful for user: {username}")

    except Exception as e:
        login_results.append(
            f"Login failed for user: {username} - Reason: {str(e)}")

    driver.get("https://www.saucedemo.com/")

# Create Log file
with open("data/User_Log.log", "w") as log_file:
    log_file.write("\nLogin Results:\n")
    for result in login_results:
        log_file.write(result + "\n")


time.sleep(2)
driver.close()
