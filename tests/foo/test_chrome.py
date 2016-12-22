import foo


def test_first(foo_fixture: foo.FooRequestsClass):
    """"""
    assert foo_fixture.init_errcode == 200


def test_zz_another(foo_fixture: foo.FooRequestsClass):
    res = foo_fixture.make_request()
    assert res.status_code == 200
