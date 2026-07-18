from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    """
    Класс Page Object для страницы корзины
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы элементов
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.cart_item_names = (By.CLASS_NAME, "inventory_item_name")
        self.cart_item_prices = (By.CLASS_NAME, "inventory_item_price")

    def open(self):
        """Открывает страницу корзины"""
        self.driver.get("https://www.saucedemo.com/cart.html")
        return self

    def proceed_to_checkout(self):
        """Нажимает кнопку Checkout"""
        self.driver.find_element(*self.checkout_button).click()
        return self

    def get_cart_items_count(self):
        """
        Получает количество товаров в корзине

        Returns:
            int: Количество товаров
        """
        return len(self.driver.find_elements(*self.cart_items))

    def get_cart_item_names(self):
        """
        Получает список названий товаров в корзине

        Returns:
            list: Список названий товаров
        """
        items = self.driver.find_elements(*self.cart_item_names)
        return [item.text for item in items]

    def get_cart_total(self):
        """
        Получает общую сумму товаров в корзине без налога

        Returns:
            float: Общая сумма
        """
        prices = self.driver.find_elements(*self.cart_item_prices)
        total = 0
        for price in prices:
            price_text = price.text.replace('$', '')
            total += float(price_text)
        return total
