from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait


def SmoothScroll(driver, scroll_step=10, scroll_pause=0.01):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(f"window.scrollBy(0, {scroll_step})")
        time.sleep(scroll_pause)

        new_height = driver.execute_script("return window.pageYOffset + window.innerHeight")
        total_height = driver.execute_script("return document.body.scrollHeight")

        if new_height >= total_height:
            break

        last_height = total_height

def ClickPresence(driver):
    try:
        presensi_button = driver.find_elements(By.XPATH, "//strong[contains(text(),'Masuk Kelas')]")
        for button in presensi_button:
            button.click()
            time.sleep(5)
            driver.back()
            return
    except Exception as e:
        print(f"Error in ClickPresence: {e}")

def LoopDiv(driver):
    time.sleep(2)
    #parent_div = driver.find_element(By.XPATH, "//div[@class='row' and contains(@style,'background-color:#FFFFFF')]")
    # all_divs = parent_div.find_elements(By.TAG_NAME, "div")
    # div_arrays =[]
    # for index, div in enumerate(all_divs):
    #     div_info = {
    #         "index": index + 1,  #start from 1?
    #         "div":div,
    #         "text": div.get_attribute("text"),
    #         "outerHTML":div.get_attribute("outerHTML"),
    #     }
    #     div_arrays.append(div_info)
    #
    # first_two_divs = div_arrays[:3]
    # for div_array in first_two_divs:
    #     print(f" Div #{div_array['index']}: \n Text: {div_array['text']} \n HTML: {div_array['outerHTML']}")
    #
    # return div_arrays

    # Locate the parent div
    parent_div = driver.find_element(By.XPATH, "//div[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12 ']")

    # Get all the children divs within the parent
    all_child_divs = parent_div.find_elements(By.XPATH, "./div")

    # Store them in an array
    div_arrays = []

    for index, div in enumerate(all_child_divs):
        div_info = {
            "index": index + 1,  # Start numbering from 1
            "text": div.get_attribute("textContent"),  # Text inside the div
            "outerHTML": div.get_attribute("outerHTML"),  # Complete HTML of the div
        }
        div_arrays.append(div_info)

    # Get only the first two divs from the list (if they exist)
    if len(div_arrays) >= 2:
        first_two_divs = div_arrays[:2]
    else:
        first_two_divs = div_arrays

    # Print details for the first two divs
    for div_array in first_two_divs:
        print(f"Div #{div_array['index']}:\nText: {div_array['text']}\nHTML: {div_array['outerHTML']}\n")

    return first_two_divs