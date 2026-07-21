from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Класс Page Object для страницы оформления заказа
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы для первой страницы оформления (информация о покупателе)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

        # Локаторы для второй страницы оформления (подтверждение)
        self.finish_button = (By.ID, "finish")
        self.cancel_button = (By.ID, "cancel")

        # Локаторы для отображения итоговой стоимости
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
        self.tax_label = (By.CLASS_NAME, "summary_tax_label")

        # Локаторы для успешного оформления
        self.complete_header = (By.CLASS_NAME, "complete-header")

    def open(self):
        """Открывает страницу оформления заказа"""
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        return self

    def fill_checkout_info(self, first_name, last_name, postal_code):
        """
        Заполняет информацию о покупателе

        Args:
            first_name (str): Имя
            last_name (str): Фамилия
            postal_code (str): Почтовый индекс
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input)\
            .send_keys(postal_code)
        return self

    def continue_checkout(self):
        """Нажимает кнопку Continue"""
        self.driver.find_element(*self.continue_button).click()
        return self

    def finish_checkout(self):
        """Нажимает кнопку Finish для завершения оформления"""
        self.driver.find_element(*self.finish_button).click()
        return self

    def get_total_amount(self):
        """
        Получает итоговую стоимость (Total)

        Returns:
            float: Итоговая стоимость
        """
        total_element = self.wait.until(
            EC.presence_of_element_located(self.total_label)
        )
        total_text = total_element.text
        # Текст имеет формат "Total: $58.29"
        total_value = total_text.split('$')[1]
        return float(total_value)

    def get_subtotal(self):
        """
        Получает промежуточную сумму (Item total)

        Returns:
            float: Промежуточная сумма
        """
        subtotal_element = self.driver.find_element(*self.subtotal_label)
        subtotal_text = subtotal_element.text
        subtotal_value = subtotal_text.split('$')[1]
        return float(subtotal_value)

    def get_tax(self):
        """
        Получает сумму налога

        Returns:
            float: Сумма налога
        """
        tax_element = self.driver.find_element(*self.tax_label)
        tax_text = tax_element.text
        tax_value = tax_text.split('$')[1]
        return float(tax_value)

    def is_checkout_complete(self):
        """
        Проверяет, успешно ли завершено оформление заказа

        Returns:
            bool: True если оформление успешно завершено
        """
        try:
            self.wait.until(
                EC.presence_of_element_located(self.complete_header))
            return True
        except Exception:
            return False
