import betamax
import pytest
import foo

foo_object = None

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'tests/fixtures/cassettes'

    # config.default_cassette_options['match_requests_on'] = [
    #     'method',
    #     'uri',
    #     # 'body'
    # ]
    #
    # config.default_cassette_options['record_mode'] = 'all'


@pytest.fixture
def foo_fixture(betamax_session):
    global foo_object
    if foo_object:
        return foo_object
        # WTF!!! when returning this store, its session.adapters are DIFFERENT (original requests' instead of betamax)!!
    else:
        betamax_session.headers.update({'Accept-Encoding': 'identity'})
        foo_object = foo.FooRequestsClass(betamax_session)
        foo_object.init_request()
        return foo_object
