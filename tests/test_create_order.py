from data import ENDPOINTS, TextMessage, Order
import pytest
import allure
from api.check_api_methods import CheckMethods, StatusCode
from api.base_api_methods import BaseApiMethods


@allure.feature("Проверка ручки создания заказа")
class TestCreateOrder:
    @allure.title("Проверка создания заказов для авторизированных пользователей с/без ингридиентов")
    @allure.description("Создаем данные для пользователя, отправляем запрос на создание пользователя, отправляем "
                        "запрос на создание заказа с токеном созданного ранее пользователя, проверяем различные "
                        "сценарии с/без ингридиентов, проверяем код ответа, проверяем "
                        "текст ответа")
    @pytest.mark.parametrize('ingredients, status_code, text_answer',
                             [(Order.INGREDIENTS, StatusCode.CODE_200, TextMessage.SUCCESS_TEXT),
                              (Order.INGREDIENTS_EMPTY, StatusCode.CODE_400, TextMessage.FALSE_TEXT)],
                             ids=["with_ingredients", "without_ingredients"])
    def test_create_order_authorized_with_or_no_ingredients(self, create_new_user_with_delete, ingredients, status_code,
                                                            text_answer):
        payload_order = {"ingredients": ingredients}
        response = BaseApiMethods.post_request(ENDPOINTS.CREATE_OR_GET_ORDER, payload_order,
                                               create_new_user_with_delete[1].json()['accessToken'])
        CheckMethods.check_status_code(response, status_code)
        CheckMethods.check_json_message(response, TextMessage.SUCCESS_KEY, text_answer)

    @allure.title("Проверка создания заказов для не авторизированных пользователей с/без ингридиентов")
    @allure.description("Создаем данные для пользователя, отправляем запрос на создание пользователя, отправляем "
                        "запрос на создание заказа без токена, проверяем различные сценарии с/без ингридиентов, "
                        "проверяем код ответа, проверяем текст ответа")
    @pytest.mark.parametrize('ingredients, status_code, text_answer',
                             [(Order.INGREDIENTS, StatusCode.CODE_200, TextMessage.SUCCESS_TEXT),
                              (Order.INGREDIENTS_EMPTY, StatusCode.CODE_400, TextMessage.FALSE_TEXT)],
                             ids=["with_ingredients", "without_ingredients"])
    def test_create_order_unauthorized_with_or_no_ingredients(self, create_new_user_with_delete, ingredients, status_code,
                                                              text_answer):
        payload_order = {"ingredients": ingredients}
        response = BaseApiMethods.post_request(ENDPOINTS.CREATE_OR_GET_ORDER, payload_order)
        CheckMethods.check_status_code(response, status_code)
        CheckMethods.check_json_message(response, TextMessage.SUCCESS_KEY, text_answer)

    @allure.title("Проверка создания заказа для авторизированного пользователя с некорректным игридиентом")
    @allure.description("Создаем данные для пользователя, отправляем запрос на создание пользователя, отправляем "
                        "запрос на создание заказа с токеном и некорректным хэшем ингредиента, проверяем код ответа, "
                        "проверяем текст ответа")
    def test_create_order_authorized_ingredients_wrong_hash(self, create_new_user_with_delete):
        payload_order = {"ingredients": Order.INGREDIENTS_WRONG}
        response = BaseApiMethods.post_request(ENDPOINTS.CREATE_OR_GET_ORDER, payload_order,
                                               create_new_user_with_delete[1].json()['accessToken'])
        CheckMethods.check_status_code(response, StatusCode.CODE_500)
        CheckMethods.check_text_message(response, TextMessage.SERVER_ERROR)

    @allure.title("Проверка создания заказа для не авторизированного пользователя с некорректным игридиентом")
    @allure.description("Создаем данные для пользователя, отправляем запрос на создание пользователя, отправляем "
                        "запрос на создание заказа без токена и некорректным хэшем ингредиента, проверяем код ответа, "
                        "проверяем текст ответа")
    def test_create_order_unauthorized_ingredients_wrong_hash(self, create_new_user_with_delete):
        payload_order = {"ingredients": Order.INGREDIENTS_WRONG}
        response = BaseApiMethods.post_request(ENDPOINTS.CREATE_OR_GET_ORDER, payload_order)
        CheckMethods.check_status_code(response, StatusCode.CODE_500)
        CheckMethods.check_text_message(response, TextMessage.SERVER_ERROR)
