import requests


class FooRequestsClass:
    def __init__(self, session: requests.Session):
        super().__init__()
        self.session = session
        self.init_errcode = 0

    def make_request(self):
        # return self.session.get("https://calendar.google.com")
        return self.session.get("https://yahoo.com")

    def init_request(self):
        res = self.session.get("https://www.google.com?q=test")
        self.init_errcode = res.status_code
