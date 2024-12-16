import requests

class APIClient:
    def __init__(self, url, username, password):
        self.base_url = None
        self.base_url = self.base_url
        self.auth = (username, password)

class APIError(Exception):
    def __init__(self, message):
        self.message = message
