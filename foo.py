import requests


class FooRequestsClass:
    def __init__(self, session: requests.Session):
        super().__init__()
        self.session = session
        self.init_errcode = 0

    def init_request(self):
        """ This will be run in conftest.py, it is the 'authentication' method. """
        res = self.session.get("https://www.google.com?q=test")
        self.init_errcode = res.status_code

    def make_request(self):
        """ This will be run as needed. """
        # return self.session.get("https://calendar.google.com")
        return self.session.get("https://yahoo.com")
