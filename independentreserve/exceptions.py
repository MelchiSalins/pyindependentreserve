from requests.exceptions import HTTPError
import logging


def http_exception_handler(f):
    """
    Decorator to keep try catch block dry for all API calls.

    :param f: function being wrapped
    :return:
    """
    def wrapper(*args, **kwargs):
        try:
            response = f(*args, **kwargs)
            response.raise_for_status()
            return response.json()
        except HTTPError as error:
            logging.error(error.message)
        except Exception as error:
            logging.error(error.message)

    return wrapper
