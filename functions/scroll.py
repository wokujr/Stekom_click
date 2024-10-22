from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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

def ClickPresence(driver):
    try:
        presensi_button = driver.find_elements(By.XPATH, "//a[contains(text(),'Presensi')]")
        for button in presensi_button:
            button.click()
            time.sleep(5)
            driver.back()
            return
    except StaleElementReferenceException:
        print("Stale element reference error")
        presensi_button = driver.find_elements_by_xpath("//a[contains(text(), 'Presensi')]")
        presensi_button.click()
