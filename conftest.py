import pytest
from data import ENDPOINTS, Order
from helpers import ProfileMethods
from api.base_api_methods import BaseApiMethods
from api.check_api_methods import CheckMethods, StatusCode


@pytest.fixture
def create_new_user_with_delete():
    user_data = ProfileMethods.generate_user()
    response = BaseApiMethods.post_request(ENDPOINTS.CREATE_USER, user_data)
    CheckMethods.check_status_code(response, StatusCode.CODE_200)
    yield user_data, response
    response_delete = BaseApiMethods.delete_request(ENDPOINTS.DELETE_USER_OR_CHANGE_INFO,
                                                    response.json()['accessToken'])
    CheckMethods.check_status_code(response_delete, StatusCode.CODE_202)


@pytest.fixture
def create_order(create_new_user_with_delete):
    payload_order = {"ingredients": Order.INGREDIENTS}
    response_order = BaseApiMethods.post_request(ENDPOINTS.CREATE_OR_GET_ORDER, payload_order,
                                                 create_new_user_with_delete[1].json()['accessToken'])
    CheckMethods.check_status_code(response_order, StatusCode.CODE_200)
    return response_order
