import pytest
import allure
from data import ENDPOINTS, TextMessage, Profile
from api.check_api_methods import CheckMethods, StatusCode
from api.base_api_methods import BaseApiMethods


@allure.feature("Проверка ручки изменения данных пользователя")
class TestChangeUserData:
    @allure.title("Проверка успешного изменения данных пользователя")
    @allure.description("Создаем данные для пользователя, отправляем запрос на создание пользователя, изменяем "
                        "данные, проверяем код ответа, проверяем текст ответа")
    @pytest.mark.parametrize('key_field, new_data', [("name", Profile.NEW_NAME),
                                                     ("password", Profile.NEW_PASSWORD),
                                                     ("email", Profile.NEW_EMAIL)],
                             ids=["change_name", "change_password", "change_email"])
    def test_change_user_data_success_new_data(self, create_new_user_with_delete, key_field, new_data):
        payload_data = {key_field: new_data}
        response = BaseApiMethods.patch_request(ENDPOINTS.DELETE_USER_OR_CHANGE_INFO, payload_data,
                                                create_new_user_with_delete[1].json()['accessToken'], )
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_json_message(response, TextMessage.SUCCESS_KEY, TextMessage.SUCCESS_TEXT)

    @allure.title("Проверка получения ошибки при изменении данных пользователя без авторизации")
    @allure.description("Создаем данные для пользователя, отправляем запрос на создание пользователя, изменяем "
                        "данные без авторизации, проверяем код ответа, проверяем текст ответа")
    @pytest.mark.parametrize('key_field, new_data', [("name", Profile.NEW_NAME),
                                                     ("password", Profile.NEW_PASSWORD),
                                                     ("email", Profile.NEW_EMAIL)],
                             ids=["change_name", "change_password", "change_email"])
    def test_change_user_data_no_authorization_error(self, create_new_user_with_delete, key_field, new_data):
        payload_data = {key_field: new_data}
        response = BaseApiMethods.patch_request(ENDPOINTS.DELETE_USER_OR_CHANGE_INFO, payload_data)
        CheckMethods.check_status_code(response, StatusCode.CODE_401)
        CheckMethods.check_json_message(response, TextMessage.MESSAGE_KEY, TextMessage.NO_AUTHORIZATION)
