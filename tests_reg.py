from tests_api import TestsApi
from common import *


class TestsReg:
    """Проверки регистрации"""

    def __init__(self, test_api):
        self._test_api = test_api
        self._test_api.turn_to_registration()
        self.current_email = self._test_api.get_random_email()

    # Проверка регистрации с некорректными данными в поле Имя
    def test_except_name_with_email_fail(self):
        self._test_api.refresh()
        assert self._test_api.check_reg(NAME_SUCCESS, SURNAME_FAIL_ARR[0], EMAIL_FAIL_ARR[0], PASS_FAIL_ARR[0], PASS_FAIL_ARR[0]) == RESULT_NEGATIVE

    # Проверка регистрации с некорректными данными в поле Фамилия
    def test_except_name_with_phone_fail(self):
        self._test_api.refresh()
        assert self._test_api.check_reg(NAME_SUCCESS, SURNAME_FAIL_ARR[1], PHONE_FAIL_ARR[0], PASS_FAIL_ARR[1], PASS_FAIL_ARR[1]) == RESULT_NEGATIVE

    # Проверка регистрации с некорректными данными в поле Email
    def test_except_phone_confirmpass_fail(self):
        self._test_api.refresh()
        assert self._test_api.check_reg(NAME_FAIL_ARR[0], SURNAME_FAIL_ARR[2], PHONE_SUCCESS, PASS_FAIL_ARR[2], PASS_SUCCESS) == RESULT_NEGATIVE

    # Проверка регистрации с некорректными данными в поле Телефон
    def test_except_surname_pass_with_phone_fail(self):
        self._test_api.refresh()
        assert self._test_api.check_reg(NAME_FAIL_ARR[1], SURNAME_SUCCESS, PHONE_FAIL_ARR[1], PASS_SUCCESS, PASS_FAIL_ARR[2]) == RESULT_NEGATIVE

    # Проверка регистрации с некорректными данными в поле Пароль
    def test_except_email_confirmpass_fail(self):
        self._test_api.refresh()
        assert self._test_api.check_reg(NAME_FAIL_ARR[2], SURNAME_FAIL_ARR[3], self.current_email, PASS_FAIL_ARR[3], PASS_SUCCESS) == RESULT_NEGATIVE

    # Проверка регистрации с некорректными данными в поле Повтор пароля
    def test_except_surname_pass_with_email_fail(self):
        self._test_api.refresh()
        assert self._test_api.check_reg(NAME_FAIL_ARR[3], SURNAME_SUCCESS, EMAIL_FAIL_ARR[1], PASS_SUCCESS, PASS_FAIL_ARR[3]) == RESULT_NEGATIVE

    # Проверка регистрации с корректными данными
    def test_success(self):
        self._test_api.refresh()
        assert self._test_api.check_reg(NAME_SUCCESS, SURNAME_SUCCESS, self.current_email, PASS_SUCCESS, PASS_SUCCESS) == RESULT_POSITIVE

    # Проверка регистрации нового пользоваьтеля с уже зарегестрированным email
    def test_user_exists(self):
        self._test_api.refresh()
        assert self._test_api.check_reg(NAME_SUCCESS, SURNAME_SUCCESS, self.current_email, PASS_SUCCESS, PASS_SUCCESS) == RESULT_USER_EXISTS