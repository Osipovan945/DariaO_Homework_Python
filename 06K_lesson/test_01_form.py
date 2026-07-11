from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Safari()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.presence_of_element_located((
            By.NAME, "first-name"
            ))).send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "zip-code").send_keys("")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        submit_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
            )
        submit_button.click()

        zip_code_field = wait.until(EC.presence_of_element_located((
            By.ID, "zip-code"
            )))
        assert "alert-danger" in zip_code_field.get_attribute("class"), (
            "Zip code поле не подсвечено красным"
        )

        fields_to_check = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company"
        ]

        for field_name in fields_to_check:
            field = driver.find_element(By.ID, field_name)
            assert "alert-success" in field.get_attribute("class"), (
                f"Поле {field_name} не подсвечено зеленым"
            )

        print("Все проверки пройдены успешно!")

    finally:
        driver.quit()
