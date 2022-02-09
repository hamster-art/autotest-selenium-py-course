import pytest
import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_basket_btn(browser):
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
