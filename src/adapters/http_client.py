import requests

class HttpClient():
    def __init__(self, base_url, default_headers = {}):
        self.base_url = base_url
        self.default_headers = default_headers

    def get(self, endpoint):
        url = self.base_url + endpoint
        r = requests.get(url)

        return { "status": r.status_code, "body": r.text }