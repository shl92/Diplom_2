import pytest
from data import ENDPOINTS, Order, URLS
from helpers import ProfileMethods
from api.base_api_methods import BaseApiMethods


@pytest.fixture
def create_new_user_with_delete():
    user_data = ProfileMethods.generate_user()
    response = BaseApiMethods.post_request(URLS.MAIN_PAGE_URL + ENDPOINTS.CREATE_USER, user_data)
    yield user_data, response
    BaseApiMethods.delete_request(URLS.MAIN_PAGE_URL + ENDPOINTS.DELETE_USER_OR_CHANGE_INFO,
                                  response.json()['accessToken'])


@pytest.fixture
def create_order(create_new_user_with_delete):
    payload_order = {"ingredients": Order.INGREDIENTS}
    response_order = BaseApiMethods.post_request(URLS.MAIN_PAGE_URL + ENDPOINTS.CREATE_OR_GET_ORDER, payload_order,
                                                 create_new_user_with_delete[1].json()['accessToken'])
    return response_order
