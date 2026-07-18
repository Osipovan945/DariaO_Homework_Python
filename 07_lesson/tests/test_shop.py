import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestShop:
    """
    Тесты для интернет-магазина с использованием Page Object
    """

    @pytest.fixture
    def driver(self):
        """Фикстура для настройки и закрытия драйвера"""
        options = Options()
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    def test_shop_checkout_total(self, driver):
        """
        Тест проверяет оформление заказа в интернет-магазине:
        1. Авторизация под пользователем standard_user
        2. Добавление 3-х товаров в корзину
        3. Переход в корзину и оформление заказа
        4. Проверка итоговой суммы
        """
        # Создаем объекты страниц
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # Шаг 1: Открываем страницу авторизации и входим
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Шаг 2: Добавляем товары в корзину
        products_page.add_product_to_cart("Sauce Labs Backpack")
        products_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        products_page.add_product_to_cart("Sauce Labs Onesie")

        # Проверяем, что в корзине 3 товара
        cart_count = products_page.get_cart_count()
        assert cart_count == 3, (
            f"В корзине должно быть 3 товара, а не {cart_count}"
        )

        # Шаг 3: Переходим в корзину
        products_page.go_to_cart()

        # Проверяем, что в корзине 3 товара
        items_count = cart_page.get_cart_items_count()
        assert items_count == 3, (
            f"В корзине должно быть 3 товара, а не {items_count}"
        )

        # Шаг 4: Нажимаем Checkout
        cart_page.proceed_to_checkout()

        # Шаг 5: Заполняем форму данными
        checkout_page.fill_checkout_info("John", "Doe", "12345")
        checkout_page.continue_checkout()

        # Шаг 6: Получаем итоговую стоимость
        total = checkout_page.get_total_amount()

        # Шаг 7: Проверяем итоговую сумму
        expected_total = 58.29
        assert total == expected_total, (
            f"Итоговая сумма {total} не равна ожидаемой {expected_total}"
        )

        # Дополнительные проверки для наглядности
        subtotal = checkout_page.get_subtotal()
        tax = checkout_page.get_tax()

        # Проверяем, что сумма subtotal + tax = total
        assert round(subtotal + tax, 2) == total, (
            "Сумма subtotal и tax не равна total"
        )
