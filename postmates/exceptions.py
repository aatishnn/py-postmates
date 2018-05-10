"""Postmates exception classes.
"""

INVALID_PARAMS = 'invalid_params'
UNKNOWN_LOCATION = 'unknown_location'
RATE_LIMIT_EXCEEDED = 'rate_limit_exceeded'
CUSTOMER_NOT_APPROVED = 'customer_not_approved'
ACCOUNT_SUSPENDED = 'account_suspended'
NOT_FOUND = 'not_found'
SERVICE_UNAVAILABLE = 'service_unavailable'
DELIVERY_LIMIT_EXCEEDED = 'delivery_limit_exceeded'
CUSTOMER_LIMITED = 'customer_limited'
COURIERS_BUSY = 'couriers_busy'
ADDRESS_UNDELIVERABLE = 'address_undeliverable'


class PostmatesException(Exception):
    """The base Exception that all other exception classes extend."""


class APIException(PostmatesException):
    """Indicate exception that involve responses from Postmates's API."""

    def __init__(self, error_dict):
        """Initialize an instance of APIException.

        :param error_dict: error dictionary from Postmates API Response
        :param field: The input field associated with the error if available.

        """
        self.code = error_dict.get('code', None)
        self.message = error_dict.get('message', None)
        self.error_dict = error_dict

        error_str = '{}: \'{}\' ({})'.format(
            self.code, self.message, self.error_dict)
        super(APIException, self).__init__(error_str)


class ClientException(PostmatesException):
    """Exceptions that don't involve interaction with Postmates's API."""
