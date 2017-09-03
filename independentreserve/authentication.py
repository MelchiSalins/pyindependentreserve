import hmac
import hashlib


class Authentication(object):
    """
    All private API methods require authentication. All method parameters (except signature) are required to authenticate a request. There are three additional parameters which should be passed to private API methods:

    API Key
    Nonce
    Signature
    """

    def __init__(self, api_key, api_secret):
        self.key = api_key
        self.secret = api_secret
        # self.nonce = int(time.time())
        self.headers = {'Content-Type': 'application/json'}

    def _generate_signature(self, parameters):
        """
        Generates a signature required to securely POST the data to the Private endpoint

        :param parameters: Query params that get passed to the URL
        :return:
        """
        message = ','.join(parameters)

        signature = hmac.new(self.secret.encode('utf-8'),
                             msg=message.encode('utf-8'),
                             digestmod=hashlib.sha256).hexdigest().upper()
        return signature
