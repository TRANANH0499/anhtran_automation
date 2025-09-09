from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(5)

    username = driver.find_element(By.XPATH, "//input[@name='username']")
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username.send_keys("Admin")
    password.send_keys("admin123")
    login_button.click()

    sleep(10)
    driver.quit()

test_login()

