from tests_api import TestsApi
from common import *

class TestsAuth:
    """Проверки авторизации"""

    def __init__(self, test_api):
        self._test_api = test_api
        self._test_api.turn_to_auth()
        self.current_email = self._test_api.get_random_email()

    # Проверка авторизации с корректными данными - номер телефона + пароль
    def test_phone_pass_success(self):
        assert self._test_api.check_auth(TAB_PHONE_PATH, PHONE_SUCCESS, PASS_SUCCESS) == RESULT_POSITIVE

    # Проверка авторизации с корректными данными - email + пароль
    def test_email_pass_success(self):
        assert self._test_api.check_auth(TAB_EMAIL_PATH, self.current_email, PASS_SUCCESS) == RESULT_POSITIVE

    # Проверка авторизации с корректными данными - логин + пароль
    def test_login_pass_success(self):
        assert self._test_api.check_auth(TAB_LOGIN_PATH, LOGIN_SUCCESS, PASS_SUCCESS) == RESULT_POSITIVE

    # Проверка авторизации с некорректными данными -  некорректный номер телефона
    def test_phone_pass_fail(self):
        assert self._test_api.check_auth(TAB_PHONE_PATH, PHONE_FAIL_ARR[2], PASS_SUCCESS) == RESULT_NEGATIVE

    # Проверка авторизации с некорректными данными -  некорректный email
    def test_email_pass_fail(self):
        assert self._test_api.check_auth(TAB_EMAIL_PATH, EMAIL_FAIL_ARR[2], PASS_SUCCESS) == RESULT_NEGATIVE

    # Проверка авторизации с некорректными данными -  некорректный логин
    def test_login_pass_fail(self):
        assert self._test_api.check_auth(TAB_LOGIN_PATH, LOGIN_FAIL, PASS_SUCCESS) == RESULT_NEGATIVE

    # Проверка авторизации с некорректными данными -  некорректный пароль
    def test_pass_fail(self):
        assert self._test_api.check_auth(TAB_EMAIL_PATH, self.current_email, PASS_FAIL_ARR[4]) == RESULT_NEGATIVE