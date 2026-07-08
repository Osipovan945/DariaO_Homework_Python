from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()

    # Шаг 1: Открываем страницу со ссылками
    driver.get("https://httpbin.org/links/10")

    # Шаг 2: Находим все ссылки на странице (тег <a>)
    links = driver.find_elements(By.TAG_NAME, "a")

    # Шаг 3: Проверяем, что количество ссылок равно 9
    assert len(links) == 9, f"Ожидалось 9 ссылок, найдено {len(links)}"

    # Шаг 4: Проверяем, что все ссылки отображаются на странице
    for i, link in enumerate(links):
        assert link.is_displayed(), f"Ссылка #{i+1} не отображается"

    # Шаг 5: Проверяем, что текст первой ссылки содержит "1"
    first_link_text = links[0].text
    assert "1" in first_link_text, (
        f"Текст первой ссылки '{first_link_text}' не содержит '1'"
    )

    # Закрываем браузер
    driver.quit()
