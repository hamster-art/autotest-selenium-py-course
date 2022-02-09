from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    fields = browser.find_elements_by_css_selector(".form-control")
    for field in fields:
        field.send_keys("answer")

    dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir, '../file.txt')

    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

    file_field = browser.find_element_by_id("file")
    file_field.send_keys(file_path)

    btn = browser.find_element_by_class_name("btn")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
