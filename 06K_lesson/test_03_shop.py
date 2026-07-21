from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_purchase():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.presence_of_element_located(
            (By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        driver.find_element(By.ID, "checkout").click()

        wait.until(EC.presence_of_element_located(
            (By.ID, "first-name"))).send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        driver.find_element(By.ID, "continue").click()

        wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label")))
        total_element = driver.find_element(
            By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        total_amount = total_text.split("$")[1]

        assert total_amount == "58.29", \
            f"Ожидалась сумма $58.29, получена ${total_amount}"

    finally:
        driver.quit()
