import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    # 2. Найдите и нажмите на кнопку "Start"
    start_button = driver.find_element(
        By.CSS_SELECTOR, '.example #start button'
        )
    start_button.click()

    # 3. Дождитесь появления текста "Hello World!"
    wait = WebDriverWait(driver, 10)

    # Ожидаем, что в элементе появится текст "Hello World!"
    wait.until(
        EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, '.example #finish h4'
            ), 'Hello World!')
    )

    # Получаем элемент с текстом
    hello_text_element = driver.find_element(
        By.CSS_SELECTOR, '.example #finish h4'
        )

    # 4. Создаем папку screenshots
    screenshots_dir = os.path.join(os.path.dirname(__file__), 'screenshots')
    os.makedirs(screenshots_dir, exist_ok=True)

    # Сохраняем скриншот
    screenshot_path = os.path.join(
        screenshots_dir, 'dynamic_loading_success.png'
        )
    driver.save_screenshot(screenshot_path)

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    actual_text = hello_text_element.text
    expected_text = 'Hello World!'
    assert actual_text == expected_text, (
        f'Ожидался текст "{expected_text}", получен "{actual_text}"'
    )

    driver.quit()
