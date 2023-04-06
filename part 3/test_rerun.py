import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import FirefoxProfile

options = FirefoxProfile()
options.set_preference("intl.accept_languages", user_language)
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
browser = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.ID, "login_link")


@pytest.mark.flaky(reruns=2) #указываем кол-во перезапусков. есть доп.параметры, подробнее в документации
def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    time.sleep(5)
    rt = browser.find_element(By.ID, "magic_link")