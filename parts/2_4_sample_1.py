from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    btn = browser.find_element_by_id("book")
    btn.click()
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    field = browser.find_element_by_id("answer")
    field.send_keys(y)
    btn = browser.find_element_by_id("solve")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()
