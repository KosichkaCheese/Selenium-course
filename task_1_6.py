from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/registration2.html")
    input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
    input1.send_keys("meow")
    input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
    input2.send_keys("meowmeow")
    input3 = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
    input3.send_keys("meow")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    time.sleep(3)

    congratsText = browser.find_element(By.TAG_NAME, "h1").text

    assert congratsText == "Congratulations! You have successfully registered!"

finally:
    time.sleep(5)
    browser.quit()
