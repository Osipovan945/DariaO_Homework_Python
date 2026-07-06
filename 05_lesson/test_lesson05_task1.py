# Откройте страницу https://httpbin.org/.

# Найдите и кликните на ссылку HTML Form.

# Проверьте, что URL изменился на /forms/post.

# Вернитесь назад на главную страницу.

# Проверьте, что вернулись на исходный URL.


from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # Шаг 1: Открываем главную страницу httpbin.org
    driver.get("https://httpbin.org/")
    print(f"Начальный URL: {driver.current_url}")

    # Шаг 2: Находим и кликаем на ссылку "HTML Form"
    # Используем By.LINK_TEXT для поиска по точному тексту ссылки
    form_link = driver.find_element(By.LINK_TEXT, "HTML form")
    form_link.click()
    print(f"URL после клика: {driver.current_url}")
    
    # Шаг 3: Проверяем, что URL изменился на /forms/post
    # Используем assert для проверки условия
    assert "/forms/post" in driver.current_url, \
        f"Ожидался URL с /forms/post, получен {driver.current_url}"
    print("✓ URL успешно изменился на /forms/post")
    
    # Шаг 4: Возвращаемся назад на главную страницу
    driver.back()
    print(f"URL после возврата: {driver.current_url}")
    
    # Шаг 5: Проверяем, что вернулись на исходный URL
    assert driver.current_url == "https://httpbin.org/", \
        f"Ожидался URL https://httpbin.org/, получен {driver.current_url}"
    print("✓ Успешно вернулись на главную страницу")
    
    # Закрываем браузер
    driver.quit()
