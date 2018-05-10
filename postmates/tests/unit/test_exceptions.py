from postmates.exceptions import (
    ClientException, APIException, PostmatesException,
    INVALID_PARAMS
)


ERROR_DICT = '''
{
  "kind": "error",
  "code": "invalid_params",
  "message": "The parameters of your request were invalid.",
  "params": {
    "dropoff_name": "Dropoff name is required.",
    "dropoff_phone_number": "Dropoff phone number must be valid phone number."
  }
}
'''


class TestPostmatesException(object):
    def test_inheritance(self):
        assert isinstance(PostmatesException(), Exception)


class TestAPIException(object):
    def test_inheritance(self):
        assert isinstance(APIException({}), PostmatesException)

    def test_error_dict_init(object):
        import json
        error_dict = json.loads(ERROR_DICT)
        exc = APIException(error_dict)
        assert exc.code == INVALID_PARAMS
        assert exc.message == 'The parameters of your request were invalid.'
        assert exc.error_dict == error_dict


class TestClientException(object):
    def test_inheritance(self):
        assert isinstance(ClientException(), PostmatesException)
