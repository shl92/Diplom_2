import pytest
import allure
from data import ENDPOINTS, TextMessage, Profile
from api.check_api_methods import CheckMethods, StatusCode
from api.base_api_methods import BaseApiMethods


@allure.feature("Проверка ручки логина пользователя в системе")
class TestLoginUser:
    @allure.title("Проверка успешного логина в систему")
    @allure.description("Отправка запроса на логин в систему, проверка кода ответа, проверка тела ответа")
    def test_login_user_success(self, create_new_user_with_delete):
        user_data = {"email": create_new_user_with_delete[0]["email"],
                     "password": create_new_user_with_delete[0]["password"]}
        response = BaseApiMethods.post_request(ENDPOINTS.LOGIN_USER, user_data)
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_json_message(response, TextMessage.SUCCESS_KEY, TextMessage.SUCCESS_TEXT)

    @allure.title("Проверка получения ошибки при логине с некорректным логином/паролем")
    @allure.description("Отправка запроса на логин в систему с некорректными логином/паролем, проверка кода ответа, "
                        "проверка текста ответа")
    @pytest.mark.parametrize("email, password", [(Profile.EMAIL, Profile.WRONG_PASSWORD),
                                                 (Profile.WRONG_EMAIL, Profile.PASSWORD)],
                             ids=['wrong_password', 'wrong_email'])
    def test_login_user_wrong_data(self, email, password):
        user_data = {"email": email,
                     "password": password}
        response = BaseApiMethods.post_request(ENDPOINTS.LOGIN_USER, user_data)
        CheckMethods.check_status_code(response, StatusCode.CODE_401)
        CheckMethods.check_json_message(response, TextMessage.MESSAGE_KEY, TextMessage.INCORRECT_DATA)
