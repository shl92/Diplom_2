import requests


class BaseApiMethods:
    @staticmethod
    def get_request(url, data=None, token=None):
        return requests.get(url, data=data, headers={'Authorization': token})

    @staticmethod
    def post_request(url, data, token=None):
        return requests.post(url, data=data, headers={'Authorization': token})

    @staticmethod
    def delete_request(url, token):
        return requests.delete(url, headers={'Authorization': token})

    @staticmethod
    def patch_request(url, data, token=None):
        return requests.patch(url, headers={'Authorization': token}, data=data)
