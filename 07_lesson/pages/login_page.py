from selenium.webdriver.common.by import By


class LoginPage:
    """
    Класс Page Object для страницы авторизации
    https://www.saucedemo.com/
    """

    def __init__(self, driver):
        self.driver = driver

        # Локаторы элементов
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        """Открывает страницу авторизации"""
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username, password):
        """
        Выполняет вход в систему

        Args:
            username (str): Имя пользователя
            password (str): Пароль
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        return self

    def get_error_message(self):
        """
        Получает текст сообщения об ошибке

        Returns:
            str: Текст сообщения об ошибке
        """
        return self.driver.find_element(*self.error_message).text
