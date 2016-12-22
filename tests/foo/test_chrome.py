# from chrome_store.chrome_store import ChromeStore

import foo


# def test_authentication(auth_store: ChromeStore, auth):
#     """
#     Check that auth_store is properly authenticated.
#     """
#     print("RUN TEST")
#     if auth_store.client_id != auth['default_client_id'] \
#             and auth_store.client_secret != auth['default_client_secret'] \
#             and auth['code'] != auth['default_code']:
#
#         assert auth_store.refresh_token
#     else:
#         assert auth_store.refresh_token == auth['placeholder_refresh_token']
#

def test_first(auth_store: foo.FooRequestsClass):
    assert auth_store.init_errcode == 200


def test_another(auth_store: foo.FooRequestsClass):
    res = auth_store.make_request()
    assert res.status_code == 200

# def test_store(auth_store):
#     print('first is ok')
#     assert auth_store
#
#
# def test_store_another(auth_store: ChromeStore):
#     print(auth_store.refresh_token)
#     assert auth_store.refresh_token
