import foo


def test_first(auth_store: foo.FooRequestsClass):
    assert auth_store.init_errcode == 200


def test_another(auth_store: foo.FooRequestsClass):
    res = auth_store.make_request()
    assert res.status_code == 200
