import vcr
import pytest
import os

from postmates import PostmatesAPI, exceptions
from postmates.exceptions import ClientException, APIException

my_vcr = vcr.VCR(
    serializer='json',
    cassette_library_dir='postmates/tests/vcr_cassettes/',
    record_mode='new_episodes',
    decode_compressed_response=True,
    match_on=['method', 'scheme', 'host', 'port', 'path', 'query', 'body'],
)


@pytest.fixture()
def pickup_address():
    return '20 McAllister St, San Francisco, CA 94102'


@pytest.fixture()
def dropoff_address():
    return '101 Market St, San Francisco, CA 94105'


@pytest.fixture()
def invalid_address():
    return 'dnbnfw, rionwe,f 254541, USA'


@pytest.fixture()
def api():
    api_key = os.environ.get('POSTMATES_TEST_API_KEY')
    customer_id = os.environ.get('POSTMATES_TEST_CUSTOMER_ID')
    return PostmatesAPI(api_key, customer_id)


class TestPostmatesAPI(object):
    @my_vcr.use_cassette('post-delivery-quote.json')
    def test_post_delivery_quote(
        self, api, pickup_address, dropoff_address, invalid_address
    ):

        assert 'id' in api.post_delivery_quote(pickup_address, dropoff_address)

        with pytest.raises(ClientException):
            api.post_delivery_quote(None, None)

        with pytest.raises(APIException):
            api.post_delivery_quote(invalid_address, invalid_address)

        try:
            api.post_delivery_quote(invalid_address, invalid_address)

        except APIException as e:
            # Postmates have sometimes returned invalid address and sometimes
            # undeliverable location for an invalid address
            errors = (
                exceptions.UNKNOWN_LOCATION, exceptions.ADDRESS_UNDELIVERABLE)
            assert e.code in errors
