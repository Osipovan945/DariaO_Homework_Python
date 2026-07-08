from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # Шаг 1: Открываем главную страницу httpbin.org
    driver.get("https://httpbin.org/")

    # Шаг 2: Находим и кликаем на ссылку "HTML Form"
    form_link = driver.find_element(By.LINK_TEXT, "HTML form")
    form_link.click()

    # Шаг 3: Проверяем, что URL изменился на /forms/post
    assert "/forms/post" in driver.current_url, \
        f"Ожидался URL с /forms/post, получен {driver.current_url}"
    print("✓ URL успешно изменился на /forms/post")

    # Шаг 4: Возвращаемся назад на главную страницу
    driver.back()

    # Шаг 5: Проверяем, что вернулись на исходный URL
    assert driver.current_url == "https://httpbin.org/", (
        f"Ожидался URL https://httpbin.org/, получен {driver.current_url}"
    )

    # Закрываем браузер
    driver.quit()
