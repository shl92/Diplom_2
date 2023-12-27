import allure


class CheckMethods:
    @staticmethod
    @allure.step("Проверка status_code ответа")
    def check_status_code(response, code):
        assert response.status_code == code, (f"Возвращенный status_code не соответствует. Ожидаемый: {code}, "
                                              f"фактический: {response.status_code}")

    @staticmethod
    @allure.step("Проверка json-ответа по ключу 'message'")
    def check_json_message(response, key, text):
        assert response.json()[key] == text, (f"Ответ не соответствует ожидаемому, ожидалось: {text}, "
                                              f"фактический ответ: {response.json()[key]}")

    @staticmethod
    @allure.step("Проверка наличия текста в ответе на запрос")
    def check_text_message(response, text):
        assert text in response.text, (f"Ответ не соответствует ожидаемому, ожидалось наличие в ответе: {text}, "
                                       f"фактический ответ: {response.text}")


class StatusCode:
    CODE_200 = 200
    CODE_202 = 202
    CODE_400 = 400
    CODE_401 = 401
    CODE_403 = 403
    CODE_500 = 500
