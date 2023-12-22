import allure
from data import ENDPOINTS, TextMessage
from api.check_api_methods import CheckMethods, StatusCode
from api.base_api_methods import BaseApiMethods


@allure.feature("Проверка ручки получения заказов конкретного пользователя")
class TestGetOrders:
    @allure.title("Проверка успешного получения заказов авторизованного пользователя")
    @allure.description("Создаем пользователя, создаем заказ, отправляем запрос на получение ранее созданного заказа "
                        "по ранее созданному пользователю, проверяем код ответа, проверяем текст ответа")
    def test_get_order_of_authorized_user(self, create_new_user_with_delete, create_order):
        response = BaseApiMethods.get_request(ENDPOINTS.CREATE_OR_GET_ORDER,
                                              token=create_new_user_with_delete[1].json()['accessToken'])
        CheckMethods.check_status_code(response, StatusCode.CODE_200)
        CheckMethods.check_json_message(response, TextMessage.SUCCESS_KEY, TextMessage.SUCCESS_TEXT)

    @allure.title("Проверка получения ошибки при попытке получить заказ не авторизованного пользователя")
    @allure.description("Создаем пользователя, создаем заказ, отправляем запрос на получение заказа без авторизации, "
                        "проверяем код ответа, проверяем текст ответа")
    def test_get_order_of_unauthorized_user_error(self, create_new_user_with_delete, create_order):
        response = BaseApiMethods.get_request(ENDPOINTS.CREATE_OR_GET_ORDER)
        CheckMethods.check_status_code(response, StatusCode.CODE_401)
        CheckMethods.check_json_message(response, TextMessage.MESSAGE_KEY, TextMessage.NO_AUTHORIZATION)
