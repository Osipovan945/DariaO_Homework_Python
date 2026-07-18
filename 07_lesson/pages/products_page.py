from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ProductsPage:
    """
    Класс Page Object для главной страницы магазина (список товаров)
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы элементов
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
        self.product_buttons = {
            "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "Sauce Labs Bolt T-Shirt": (
                By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
        }
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def open(self):
        """Открывает главную страницу магазина"""
        self.driver.get("https://www.saucedemo.com/inventory.html")
        return self

    def add_product_to_cart(self, product_name):
        """
        Добавляет товар в корзину

        Args:
            product_name (str): Название товара
        """
        button_locator = self.product_buttons.get(product_name)
        if not button_locator:
            raise ValueError(f"Товар '{product_name}' не найден")

        self.driver.find_element(*button_locator).click()
        return self

    def go_to_cart(self):
        """Переходит в корзину"""
        self.driver.find_element(*self.cart_button).click()
        return self

    def get_cart_count(self):
        """
        Получает количество товаров в корзине

        Returns:
            int: Количество товаров в корзине
        """
        try:
            badge = self.driver.find_element(*self.cart_badge)
            return int(badge.text)
        except Exception:
            return 0
