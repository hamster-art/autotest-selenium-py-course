from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1")
    x = int(num1.text)
    num2 = browser.find_element_by_id("num2")
    y = int(num2.text)
    sum = str(x + y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)
    browser.find_element_by_class_name("btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
