from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestText(unittest.TestCase):
    def test_text1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        elements = browser.find_elements(By.CSS_SELECTOR, "input:required")
        for element in elements:
            element.send_keys("Answer")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Should be success message")

        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_text2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element(By.CSS_SELECTOR, ".first:required")
        first_name.send_keys("answer")
        last_name = browser.find_element(By.CSS_SELECTOR, ".second:required")
        last_name.send_keys("answer")
        email = browser.find_element(By.CSS_SELECTOR, ".third:required")
        email.send_keys("answer")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Should be success message 2")

        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()
