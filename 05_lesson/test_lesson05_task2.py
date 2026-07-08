from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

    # Шаг 1: Открываем страницу с формой
    driver.get("https://httpbin.org/forms/post")

    # Шаг 2: Находим поле ввода по атрибутам
    name_field = driver.find_element(By.NAME, "custname")

    # Шаг 3: Вводим имя в поле
    name_field.send_keys("Иван Петров")

    # Шаг 4: Находим и нажимаем кнопку Submit
    submit_button = driver.find_element(
        By.XPATH,
        "//button[text()='Submit order']"
    )
    submit_button.click()

    # Шаг 5: Проверяем, что URL изменился после отправки
    assert driver.current_url != "https://httpbin.org/forms/post", (
        "URL не изменился после отправки формы"
    )

    # Закрываем браузер
    driver.quit()
