# Откройте страницу https://httpbin.org/forms/post.

# Найдите поле ввода с названием custname.

# Введите в него ваше имя.

# Найдите кнопку Submit и нажмите на нее.

# Проверьте, что после нажатия URL изменился.

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():

    # Инициализация драйвера
    driver = webdriver.Chrome()
    
    # Шаг 1: Открываем страницу с формой
    driver.get("https://httpbin.org/forms/post")
    print(f"Начальный URL: {driver.current_url}")
    
    # Шаг 2: Находим поле ввода по атрибуту name="custname"  <input name="custname">
    # Используем By.NAME для поиска по атрибуту name
    name_field = driver.find_element(By.NAME, "custname")
    
    # Шаг 3: Вводим имя в поле
    # send_keys() вводит текст в поле ввода
    name_field.send_keys("Иван Петров")
    print("✓ Имя введено в поле")
    
    # Шаг 4: Находим и нажимаем кнопку Submit
    # Используем By.XPATH для поиска кнопки по тексту
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    submit_button.click()
    print("✓ Кнопка Submit нажата")
    
    # Шаг 5: Проверяем, что URL изменился после отправки
    # Даем небольшую задержку для обработки запроса (без time.sleep)
    # В реальных проектах используют WebDriverWait, но здесь это не требуется
    current_url = driver.current_url
    print(f"URL после отправки: {current_url}")
    
    # Проверяем, что URL изменился (стал другим)
    assert current_url != "https://httpbin.org/forms/post", \
        "URL не изменился после отправки формы"
    print("✓ URL успешно изменился после отправки формы")

    # Закрываем браузер
    driver.quit()
