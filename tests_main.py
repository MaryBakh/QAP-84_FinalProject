#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.storage.googleapis.com/index.html?path=2.43/
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path /tests/chrome test_selenium_simple.py
#

import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import *
from tests_auth import TestsAuth
from tests_reg import TestsReg
from tests_api import TestsApi


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    # Переходим на страницу авторизации
    pytest.driver.get(TEST_WEB_PAGE_PATH)
    pytest.driver.implicitly_wait(WAIT_TIME)

    yield

    pytest.driver.quit()


def tests_main():

    """Запуск тестов"""

    test_api = TestsApi(pytest.driver)
    test_reg = TestsReg(test_api)

    # 1 Запуск теста регистрации с корректными данными
    test_reg.test_success()

    # # 2 Запуск теста регистрации с некорректными данными в поле Имя
    # test_reg.test_except_name_with_email_fail()
    #
    # # 3 Запуск теста регистрации с некорректными данными в поле Фамилия
    # test_reg.test_except_name_with_phone_fail()
    #
    # # 4 Запуск теста регистрации с некорректными данными в поле Email
    # test_reg.test_except_phone_confirmpass_fail()
    #
    # # 5 Запуск теста регистрации с некорректными данными в поле Телефон
    # test_reg.test_except_surname_pass_with_phone_fail()
    #
    # # 6 Запуск теста регистрации с некорректными данными в поле Пароль
    # test_reg.test_except_email_confirmpass_fail()
    #
    # # 7 Запуск теста регистрации с некорректными данными в поле Повтор пароля
    # test_reg.test_except_surname_pass_with_email_fail()
    # #
    # # # 8 Запуск теста регистрации нового пользоваьтеля с уже зарегестрированным email
    # # test_reg.test_user_exists()

    test_auth = TestsAuth(test_api)

    # 9 Запуск теста авторизации с корректными данными - номер телефона + пароль
    test_auth.test_phone_pass_success()

    # 10 Запуск теста авторизации с некорректными данными -  некорректный номер телефона
    test_auth.test_phone_pass_fail()

    # 11 Запуск теста авторизации с корректными данными - email + пароль
    test_auth.test_email_pass_success()

    # 12 Запуск теста авторизации с некорректными данными -  некорректный email
    test_auth.test_email_pass_fail()

    # 13 Запуск теста авторизации с корректными данными - логин + пароль
    test_auth.test_login_pass_success()

    # 14 Запуск теста авторизации с некорректными данными -  некорректный логин
    test_auth.test_login_pass_fail()

    # 15 Запуск теста авторизации с некорректными данными -  некорректный пароль
    test_auth.test_pass_fail()






