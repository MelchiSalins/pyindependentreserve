from requests.exceptions import HTTPError
import logging


def http_exception_handler(f):

    """
    Logs error.

    :param error: error being logged
    """

    def log_error(error):
        if hasattr(error, "message"):
            logging.error(error.message)
        else:
            logging.error(error)

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
            log_error(error)
        except Exception as error:
            log_error(error)

    return wrapper
