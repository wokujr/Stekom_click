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
    # Locate the parent div
    parent_div = driver.find_element(By.XPATH, "//div[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12 ']")

    # Get all the children divs within the parent
    all_child_divs = parent_div.find_elements(By.XPATH, "./div")

    # Store them in an array
    div_arrays = []

    for index, div in enumerate(all_child_divs):
        div_info = {
            "index": index,
            "text": div.get_attribute("textContent"),       # Text inside the div
            "outerHTML": div.get_attribute("outerHTML"),    # Complete HTML of the div
        }
        div_arrays.append(div_info)

    # Get only the first two divs from the list (if they exist)
    if len(div_arrays) >= 4:
        div_subset = div_arrays[4:]
    else:
        div_subset = div_arrays

    # Print details for the first two divs
    for div_array in div_subset:
        print(f" Div #{div_array['index']}:\n Text: {div_array['text']}\n HTML: {div_array['outerHTML']}\n")

    return div_subset

def LoopAndClick(driver):
    time.sleep(2)

    # Locate the parent div
    parent_div = driver.find_element(By.XPATH, "//div[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12 ']")

    # Get all the children divs within the parent
    all_child_divs = parent_div.find_elements(By.XPATH, "./div")

    # Store them in an array
    div_arrays = []

    for index, div in enumerate(all_child_divs):
        div_info = {
            "index": index,
            "text": div.get_attribute("textContent"),       # Text inside the div
            "outerHTML": div.get_attribute("outerHTML"),    # Complete HTML of the div
            "button": div.find_element(By.XPATH, "//strong[contains(text(), 'Masuk Kelas')]")  # Find "Masuk Kelas" button inside each div
        }
        div_arrays.append(div_info)

    # Loop through the div elements, click the button, go back, and click the next button
    for div_array in div_arrays:
        # Click the "Masuk Kelas" button
        button = div_array['button']
        button.click()
        print(f"Clicked on 'Masuk Kelas' button in div #{div_array['index']}")

        # Wait for the next page to load (adjust time or use a better wait method)
        time.sleep(5)  # Replace with WebDriverWait if necessary

        # Go back to the previous page
        driver.back()
        print("Back to previous page")

        # Wait for the page to reload and divs to be available again
        time.sleep(3)

        # Re-locate the parent div and all its child divs again after navigating back
        parent_div = driver.find_element(By.XPATH, "//div[@class='col-xs-12 col-sm-12 col-md-12 col-lg-12 ']")
        all_child_divs = parent_div.find_elements(By.XPATH, "./div")

        # Store updated divs in the array again
        div_arrays = []
        for index, div in enumerate(all_child_divs):
            div_info = {
                "index": index,
                "text": div.get_attribute("textContent"),
                "outerHTML": div.get_attribute("outerHTML"),
                "button": div.find_element(By.XPATH, "//strong[contains(text(), 'Masuk Kelas')]")  # Re-fetch the buttons
            }
            div_arrays.append(div_info)

    return div_arrays