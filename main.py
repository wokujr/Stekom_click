from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv('URLSIAKAD')
username = os.getenv('USERSIAKAD')
password = os.getenv('PASSWORD')

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get(url)

nim_input = driver.find_element(By.ID, 'user_name')
nim_input.send_keys(username)

time.sleep(2)

#locate password
password_input = driver.find_element(By.ID, 'user_password')
password_input.send_keys(password)

time.sleep(2)

submit_button = driver.find_element(By.NAME, 'Submit')
submit_button.click()

def SmoothScroll(driver, scroll_step=10, scroll_pause=0.01):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(f"window.scrollBy(0, {scroll_step})")
        time.sleep(scroll_pause)

        new_height = driver.execute_script("return window.pageYOffset + window.innerHeight")
        total_height = driver.execute_script("return document.body.scrollHeight")

        if new_height >= total_height:
            break

        last_height =total_height

SmoothScroll(driver)

driver.implicitly_wait(2)
try:
    list_items = driver.find_elements(By.CSS_SELECTOR, 'li')
    for index, item in enumerate(list_items, start=1):
        item_text = item.text.strip()
        if item_text:
            print(f"{index}. {item_text}")
            if "Jadwal Kelasku" in item_text:
                jadwal_kelas_link = item.find_element(By.TAG_NAME, 'a')
                print(f"Clicking on: {item_text}")
                time.sleep(2)
                jadwal_kelas_link.click()
                break
except Exception as e:
    print(f"an Error occurred: {e}")

time.sleep(10)

driver.quit()

