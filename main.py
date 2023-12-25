from pathlib import Path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import (WebDriverException,
                                        NoSuchElementException,
                                        NoSuchWindowException)
from chromedriver_py import binary_path
import time

ROOT_FOLDER = Path(__file__).parent
service = Service(executable_path=binary_path)
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)

browser.get("https://web.whatsapp.com/")

time.sleep(20)

while True:
    cells = []
    title = ""
    message = "Essa mensagem foi enviado por um bot automatizado com \
selenium, para mais detalhes acesse: \
https://github.com/LevideAlmeida/Bot_Whatsapp"

    try:
        windows = browser.window_handles
    except WebDriverException:
        break

    try:
        cells = browser.find_elements(By.CLASS_NAME, "_2H6nH")
    except NoSuchWindowException:
        break
    except NoSuchElementException:
        time.sleep(2)

    try:
        for cell in cells:
            cell.click()
            input_box = browser.find_element(By.CLASS_NAME, "_3Uu1_")
            input_box.send_keys(message)
            input_box.send_keys(Keys.ENTER)
            time.sleep(10)
    except NoSuchWindowException:
        break
