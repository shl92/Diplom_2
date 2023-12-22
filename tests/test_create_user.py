import pytest
import allure
from data import ENDPOINTS, TextMessage
from helpers import ProfileMethods
from api.check_api_methods import CheckMethods, StatusCode
from api.base_api_methods import BaseApiMethods


@allure.feature("Проверка ручки создания пользователя")
class TestCreateUser:
    @allure.title("Проверка успешного создания пользователя")
    @allure.description("Создаем данные для пользователя, отправляем запрос на создание пользователя, проверяем код "
                        "ответа, проверяем текст ответа")
    def test_create_user_success_new_user(self):
        response = BaseApiMethods.post_request(ENDPOINTS.CREATE_USER, ProfileMethods.generate_user())
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_json_message(response, TextMessage.SUCCESS_KEY, TextMessage.SUCCESS_TEXT)

    @allure.title("Проверка получения ошибки при повторном создании уже существующего пользователя")
    @allure.description("Создаем пользователя, отправляем запрос на повторное создание существующего пользователя, "
                        "проверяем код ответа, проверяем текст ответа")
    def test_create_user_existed_user_error(self, create_new_user_with_delete):
        response = BaseApiMethods.post_request(ENDPOINTS.CREATE_USER, create_new_user_with_delete[0])
        CheckMethods.check_status_code(response, StatusCode.CODE_403)
        CheckMethods.check_json_message(response, TextMessage.MESSAGE_KEY, TextMessage.EXISTED_USER)

    @allure.title("Проверка получения ошибки при создании пользователя без email/пароля/имени")
    @allure.description("Создаем данные для пользователя, отправляем запрос на создание пользователя без email/ пароля/"
                        "имени, проверяем код ответа, проверяем текст ответа")
    @pytest.mark.parametrize('email, password, name',
                             [(ProfileMethods.generate_user()['email'], ProfileMethods.generate_user()['password'],
                               None),
                              (ProfileMethods.generate_user()['email'], None, ProfileMethods.generate_user()['name']),
                              (None, ProfileMethods.generate_user()['password'],
                               ProfileMethods.generate_user()['name'])],
                             ids=['without_email', 'without_password', 'without_name'])
    def test_create_user_not_all_data_error(self, email, password, name):
        payload_profile = {"email": email,
                           "password": password,
                           "name": name}
        response = BaseApiMethods.post_request(ENDPOINTS.CREATE_USER, payload_profile)
        CheckMethods.check_status_code(response, StatusCode.CODE_403)
        CheckMethods.check_json_message(response, TextMessage.MESSAGE_KEY, TextMessage.NOT_ALL_DATA)
