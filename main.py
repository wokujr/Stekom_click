from selenium import webdriver
from dotenv import load_dotenv
import os
from functions.automatic import *

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

SmoothScroll(driver)

driver.implicitly_wait(2)
try:
    list_items = driver.find_elements(By.CSS_SELECTOR, 'li')
    for index, item in enumerate(list_items, start=1):
        item_text = item.text.strip()
        if item_text:
            #print(f"{index}. {item_text}")
            if "Jadwal Kelasku" in item_text:
                jadwal_kelas_link = item.find_element(By.TAG_NAME, 'a')
                print(f"Clicking on: {item_text}")
                time.sleep(2)
                jadwal_kelas_link.click()
                break
except Exception as e:
    print(f"an Error occurred: {e}")

LoopDiv(driver)

time.sleep(10)

driver.quit()

