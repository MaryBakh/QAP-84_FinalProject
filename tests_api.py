import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random_mail_api import RandomMailApi
from common import *
import time


class TestsApi(object):


    def __init__(self, driver):
        self._driver = driver
        self.random_mail_api = RandomMailApi()
        self.current_mail = self.random_mail_api.get_mail()

    def check_auth(self, tab_path='', user='', passw=''):
        """ Ввод параметров и проверка успешного прохождения авторизации"""

        # Выбор типа авторизации - номер/логин/email
        self._driver.find_element(By.XPATH, tab_path).click()

        # Ввод номера/логина/email
        self._driver.find_element(By.XPATH, USER_PATH).send_keys(user)

        # Ввод пароля
        self._driver.find_element(By.XPATH, PASS_PATH).send_keys(passw)

        # Нажать на кнопку Войти
        self._driver.find_element(By.XPATH, LOGIN_BUTTON_PATH).click()

        # Проверка прохождения авторизации - должна иметься кнопка выхода
        ret = ''
        try:
            ret = self._driver.find_element(By.XPATH, LOGOUT_BUTTON_PATH).text
            if ret != '':
                # если авторизация пройдена - выход из личного кабинета
                self._driver.find_element(By.XPATH, LOGOUT_BUTTON_PATH).click()
                ret = RESULT_POSITIVE
        except Exception as e:
            # Обработка негативных тестов
            print(e)
            ret = RESULT_NEGATIVE
        return ret

    def check_reg(self, user='', surname='', email='', passw='', cpassw=''):
        """ Ввод параметров и проверка успешного прохождения регистрации"""

        # Найти поле Имя и ввести данные
        self._driver.find_element(By.NAME, USER_NAME).send_keys(user)

        # Найти поле Фамилия и ввести данные
        self._driver.find_element(By.NAME, SURNAME_NAME).send_keys(surname)

        # Найти поле email и ввести данные
        self._driver.find_element(By.XPATH, EMAIL_PATH).send_keys(email)

        # Найти поле password и ввести данные
        self._driver.find_element(By.XPATH, PASS_PATH).send_keys(passw)

        # Найти поле confirm password и ввести данные
        self._driver.find_element(By.XPATH, CONFIRM_PASS_PATH).send_keys(cpassw)

        # Попытка регистрации - нажать на кнопку Регистрация
        self._driver.find_element(By.NAME, REGISTER_BUTTON_NAME).click()

        # Сначала попадаем на страницу подтверждения емэйла
        try:
            if self._driver.find_element(By.XPATH, CONFIRM_CODE_0):
                # Подтверждаем email
                self.check_confirmation_code()
        except Exception as e:
            print(e)

        ret = ''
        try:
            # Если регистрация прошла - попадаем в личный кабинет
            ret = self._driver.find_element(By.XPATH, LOGOUT_BUTTON_PATH).text
            if ret != '':
                self._driver.find_element(By.XPATH, LOGOUT_BUTTON_PATH).click()
                self._driver.find_element(By.XPATH, REGISTER_PATH).click()
                return RESULT_POSITIVE
        except Exception as e:
            # Обработка негативных тестов
            print(e)

        # Если регистрация не прошла - это может быть потому, что пользователь уже существует
        goto_login = ''
        try:
            # Если пользователь уже существует - должна быть кнопка Войти
            goto_login = self._driver.find_element(By.NAME, GOTO_LOGIN_BUTTON_NAME).text
            if goto_login:
                # Пользователь зарегистрирован, выходим в авторизацию и далее в регистрацию
                self._driver.find_element(By.NAME, GOTO_LOGIN_BUTTON_NAME).click()
                self._driver.find_element(By.XPATH, REGISTER_PATH).click()
                return RESULT_USER_EXISTS
        except Exception as e:
            # Просто ошибка регистрации (некорректный ввод и тд)
            print(e)
            return RESULT_NEGATIVE

    def turn_to_registration(self):
        pytest.driver.get(TEST_WEB_PAGE_PATH)
        self._driver.find_element(By.XPATH, REGISTER_PATH).click()

    def turn_to_auth(self):
        pytest.driver.get(TEST_WEB_PAGE_PATH)

    def refresh(self):
        self._driver.refresh()

    def check_confirmation_code(self):
        # Ждем получения письма с кодом подтверждения
        # Времени ожидания письма с кодом подтверждения может быть недостаточно
        # Или сервис отправки письма может не отработать - в таком случае нужно подождать пару минут и перезапустить тесты
        time.sleep(10)
        # Находим сообщение по id
        id = self.random_mail_api.get_message_id(self.current_mail)
        if id != 0:
            # Если сообщение есть - находим код
            code = self.random_mail_api.get_confirmation_code(self.current_mail, id)
            # Передаем код
            self._driver.find_element(By.XPATH, CONFIRM_CODE_0).send_keys(code[0])
            self._driver.find_element(By.XPATH, CONFIRM_CODE_1).send_keys(code[1])
            self._driver.find_element(By.XPATH, CONFIRM_CODE_2).send_keys(code[2])
            self._driver.find_element(By.XPATH, CONFIRM_CODE_3).send_keys(code[3])
            self._driver.find_element(By.XPATH, CONFIRM_CODE_4).send_keys(code[4])
            self._driver.find_element(By.XPATH, CONFIRM_CODE_5).send_keys(code[5])
        else:
            raise Exception("Message not found in email box!")


    def get_random_email(self):
        return self.current_mail