from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    btn = browser.find_element_by_class_name("btn")
    btn.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    field = browser.find_element_by_id("answer")
    field.send_keys(y)
    btn = browser.find_element_by_class_name("btn")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
