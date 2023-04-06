import math
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    # login = input("Введите свой логин: ")
    login = "" #put your own data here
    # password = input("Введите свой пароль: ")
    password = "" #put your own data here
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)

    # click
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "ember33"))
    )
    button.click()

    # input
    input1 = browser.find_element(By.ID, "id_login_email")
    input1.send_keys(login)
    input1 = browser.find_element(By.ID, "id_login_password")
    input1.send_keys(password)

    # click
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "sign-form__btn"))
    )
    button.click()
    time.sleep(5)

    # put answer
    data = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "ember-text-area"))
    )
    data.clear()
    answer = math.log(int(time.time()))
    data.send_keys(answer)

    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()
    time.sleep(5)
    result = WebDriverWait(browser, 10).until(
        EC.element_to_be_selected((By.CLASS_NAME, "smart-hints__hint"))
    ).text()

    time.sleep(5)
    assert result == "Correct!"

