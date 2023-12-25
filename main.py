from pathlib import Path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import (WebDriverException,
                                        NoSuchElementException,
                                        NoSuchWindowException,
                                        StaleElementReferenceException)
from chromedriver_py import binary_path
import time

ROOT_FOLDER = Path(__file__).parent
service = Service(executable_path=binary_path)
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)

browser.get("https://web.whatsapp.com/")
break_loop = False
levi_alcancado = False
programado_alcancado = False

time.sleep(20)

while True:
    cells = []
    title = ""

    time.sleep(3)
    try:
        windows = browser.window_handles
    except WebDriverException:
        break

    try:
        cells = browser.find_elements(By.TAG_NAME, "span")
    except NoSuchWindowException:
        print("nao achou janela")
        cells = []
    except NoSuchElementException:
        print("nao achou o elemento")
        cells = []
    except NoSuchWindowException:
        break

    for cell in cells:
        try:
            title = cell.get_attribute("title")
        except StaleElementReferenceException:
            title = ""
        except NoSuchElementException:
            title = ""
        except NoSuchWindowException:
            break

        if title == "+55 85 8686-2996" and not levi_alcancado:
            print("Deu bom", title)
            cell.click()
            input_box = browser.find_element(By.CLASS_NAME, "_3Uu1_")
            input_box.send_keys("Feliz Natal")
            input_box.send_keys(Keys.ENTER)
            levi_alcancado = True
