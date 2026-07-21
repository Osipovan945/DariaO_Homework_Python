import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.calculator_page import CalculatorPage


class TestCalculator:
    """
    Тесты для калькулятора с использованием Page Object
    """

    @pytest.fixture
    def driver(self):
        """Фикстура для настройки и закрытия драйвера"""
        options = Options()
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    def test_calculator_with_delay(self, driver):
        """
        Тест проверяет работу калькулятора с задержкой:
        1. Установить задержку 45 секунд
        2. Вычислить 7 + 8
        3. Проверить, что результат равен 15
        """
        # Создаем объект страницы калькулятора
        calculator_page = CalculatorPage(driver)

        # Открываем страницу
        calculator_page.open()

        # Устанавливаем задержку 45 секунд
        calculator_page.set_delay(45)

        # Нажимаем кнопки: 7, +, 8, =
        calculator_page.click_button('7')
        calculator_page.click_button('+')
        calculator_page.click_button('8')
        calculator_page.click_button('=')

        # Ожидаем результат и проверяем его
        result = calculator_page.wait_for_result("15")

        # Проверяем, что результат равен 15
        assert result == "15", f"Ожидался результат '15', получен '{result}'"

        # Дополнительная проверка: результат должен быть числом
        assert result.isdigit(), "Результат должен быть числом"
