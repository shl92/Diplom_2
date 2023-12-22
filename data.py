from dataclasses import dataclass
from helpers import ProfileMethods


class ENDPOINTS:
    CREATE_USER = "https://stellarburgers.nomoreparties.site/api/auth/register"
    DELETE_USER_OR_CHANGE_INFO = "https://stellarburgers.nomoreparties.site/api/auth/user"
    LOGIN_USER = "https://stellarburgers.nomoreparties.site/api/auth/login"
    CREATE_OR_GET_ORDER = "https://stellarburgers.nomoreparties.site/api/orders"


@dataclass
class Profile:
    EMAIL: str = "alex_shl@yandex.ru"
    WRONG_EMAIL: str = "unexisted_email@ya.ru"
    PASSWORD: str = "19920911"
    WRONG_PASSWORD: str = "1234567"
    NAME: str = "Alex"
    NEW_NAME: str = ProfileMethods.generate_user()["name"]
    NEW_EMAIL: str = ProfileMethods.generate_user()["email"]
    NEW_PASSWORD: str = ProfileMethods.generate_user()["password"]


class TextMessage:
    SUCCESS_TEXT = True
    FALSE_TEXT = False
    SUCCESS_KEY = 'success'
    MESSAGE_KEY = 'message'
    USER_NAME_KEY = []
    EXISTED_USER = 'User already exists'
    NOT_ALL_DATA = "Email, password and name are required fields"
    INCORRECT_DATA = "email or password are incorrect"
    NO_AUTHORIZATION = "You should be authorised"
    SERVER_ERROR = "Internal Server Error"


class Order:
    INGREDIENTS = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    INGREDIENTS_EMPTY = ""
    INGREDIENTS_WRONG = ["11111111111111"]
