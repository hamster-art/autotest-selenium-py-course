import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def answer():
    return str(math.log(int(time.time())))


links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]

@pytest.fixture(scope="function")
def browser():
    print("\nStart browser ...")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser ...")
    browser.quit()

@pytest.mark.parametrize("link", links)
def test_stepik(browser, link):
    browser.get(link)
    browser.implicitly_wait(15)
    textarea = browser.find_element(By.CLASS_NAME, "textarea")
    textarea.send_keys(answer())
    btn = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    btn.click()
    feedback = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    feedback_text = feedback.text
    assert feedback_text == "Correct!", f"Error, not correct {link}"
