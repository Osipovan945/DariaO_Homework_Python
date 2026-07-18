from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

        # Локаторы элементов
        self.delay_input = (By.ID, "delay")
        self.display = (By.CLASS_NAME, "screen")
        self.buttons = {
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '+': (By.XPATH, "//span[text()='+']"),
            '=': (By.XPATH, "//span[text()='=']"),
        }

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
                        "slow-calculator.html")
        return self

    def set_delay(self, seconds):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(seconds))
        return self

    def click_button(self, button_text):
        button_locator = self.buttons.get(button_text)
        if not button_locator:
            raise ValueError(f"Кнопка '{button_text}' не найдена")

        button = self.driver.find_element(*button_locator)
        button.click()
        return self

    def get_result(self):
        display_element = self.wait.until(
            EC.presence_of_element_located(self.display)
        )
        return display_element.text

    def wait_for_result(self, expected_value):
        def result_matches(driver):
            display = driver.find_element(*self.display)
            return display.text == expected_value

        self.wait.until(result_matches)
        return self.get_result()
