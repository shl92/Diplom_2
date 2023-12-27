import pytest
import allure
from data import ENDPOINTS, TextMessage, Profile, URLS
from api.check_api_methods import CheckMethods, StatusCode
from api.base_api_methods import BaseApiMethods


@allure.feature("Проверка ручки изменения данных пользователя")
class TestChangeUserData:
    @allure.title("Проверка успешного изменения данных пользователя")
    @allure.description("Запросы валидного (с авторизацией) изменения данных пользователя, ожидаемый успешный статус "
                        "ответа (200) и текст ответа 'True'")
    @pytest.mark.parametrize('key_field, new_data', [("name", Profile.NEW_NAME),
                                                     ("password", Profile.NEW_PASSWORD),
                                                     ("email", Profile.NEW_EMAIL)],
                             ids=["change_name", "change_password", "change_email"])
    def test_change_user_data_success_new_data(self, create_new_user_with_delete, key_field, new_data):
        payload_data = {key_field: new_data}
        response = BaseApiMethods.patch_request(URLS.MAIN_PAGE_URL + ENDPOINTS.DELETE_USER_OR_CHANGE_INFO, payload_data,
                                                create_new_user_with_delete[1].json()['accessToken'], )
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_json_message(response, TextMessage.SUCCESS_KEY, TextMessage.SUCCESS_TEXT)

    @allure.title("Проверка получения ошибки при изменении данных пользователя без авторизации")
    @allure.description("Запросы невалидного (без авторизации) изменения данных пользователя, ожидаем ошибку клиента "
                        "(401) и текста ответа 'You should be authorised'")
    @pytest.mark.parametrize('key_field, new_data', [("name", Profile.NEW_NAME),
                                                     ("password", Profile.NEW_PASSWORD),
                                                     ("email", Profile.NEW_EMAIL)],
                             ids=["change_name", "change_password", "change_email"])
    def test_change_user_data_no_authorization_error(self, create_new_user_with_delete, key_field, new_data):
        payload_data = {key_field: new_data}
        response = BaseApiMethods.patch_request(URLS.MAIN_PAGE_URL + ENDPOINTS.DELETE_USER_OR_CHANGE_INFO, payload_data)
        CheckMethods.check_status_code(response, StatusCode.CODE_401)
        CheckMethods.check_json_message(response, TextMessage.MESSAGE_KEY, TextMessage.NO_AUTHORIZATION)
