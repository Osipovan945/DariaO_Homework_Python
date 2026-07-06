# Откройте страницу https://httpbin.org/links/10.

# Найдите все ссылки на странице (тег <a> ).

# Проверьте, что количество ссылок равно 9.

# Проверьте, что все ссылки отображаются на странице.

# Проверьте, что текст первой ссылки содержит "1"

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    # Инициализация драйвера
    driver = webdriver.Chrome()

    # Шаг 1: Открываем страницу со ссылками
    driver.get("https://httpbin.org/links/10")
    print(f"Открыта страница: {driver.current_url}")

    # Шаг 2: Находим все ссылки на странице (тег <a>)
    # find_elements (во множественном) возвращает список всех найденных элементов
    links = driver.find_elements(By.TAG_NAME, "a")

    # Шаг 3: Проверяем, что количество ссылок равно 9
    # Используем assert для проверки количества
    expected_count = 9
    actual_count = len(links)
    assert actual_count == expected_count, \
        f"Ожидалось {expected_count} ссылок, найдено {actual_count}"
    print(f"✓ Количество ссылок: {actual_count} (ожидалось {expected_count})")

    # Шаг 4: Проверяем, что все ссылки отображаются на странице
    # Используем цикл для проверки каждой ссылки
    all_visible = True
    for i, link in enumerate(links):
        # is_displayed() проверяет, видим ли элемент на странице
        if not link.is_displayed():
            all_visible = False
            print(f"  Ссылка #{i+1} не отображается")
            break

    assert all_visible, "Не все ссылки отображаются на странице"
    print("✓ Все ссылки отображаются на странице")

    # Шаг 5: Проверяем, что текст первой ссылки содержит "1"
    # Используем индекс [0] для доступа к первой ссылке
    first_link_text = links[0].text
    assert "1" in first_link_text, \
        f"Текст первой ссылки '{first_link_text}' не содержит '1'"
    print(f"✓ Текст первой ссылки содержит '1': '{first_link_text}'")

    # Дополнительно выведем информацию о всех ссылках для наглядности
    print("\nИнформация о найденных ссылках:")
    for i, link in enumerate(links):
        print(
            f"  Ссылка #{i+1}: текст='{link.text}',"
            f"href='{link.get_attribute('href')}'"
            )

    # Закрываем браузер
    driver.quit()
