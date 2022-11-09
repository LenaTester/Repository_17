from pythonProject.Repository_16.books_and_roles.config import config
import requests


class BaseAPI:

    def __init__(self):
        self.base_url = config['base_url']
        self.headers = None
        self.request = requests

    def get(self, url, body=None, headers=None, params=None):
        response = self.request.get(f"{self.base_url}{url}", data=body, headers=headers, params=params)
        return response

    def post(self, url, json=None, headers=None, params=None):
        response = self.request.post(f"{self.base_url}{url}", json, headers=headers, params=params)
        return response

    def put(self, url, json=None, headers=None, params=None):
        response = self.request.put(f"{self.base_url}{url}", json, headers=headers, params=params)
        return response

    def delete(self, url, headers=None, params=None):
        response = self.request.delete(f"{self.base_url}{url}", headers=headers, params=params)
        return response
