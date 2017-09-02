import requests
import hmac, hashlib
import json
import time
from collections import OrderedDict

from .authentication import Authentication
from .exceptions import http_exception_handler


class PrivateMethods(Authentication):
    def __init__(self, api_key, api_secret):
        super(PrivateMethods, self).__init__(api_key, api_secret)

    @http_exception_handler
    def get_open_orders(self, primary_currency_code="Xbt", secondary_currency_code="Aud", page_index=1, page_size=10):
        """
        Retrieves a page of a specified size, with your currently Open and Partially Filled orders.
        :return:
        """

        nonce = int(time.time())
        url = "https://api.independentreserve.com/Private/GetOpenOrders"

        parameters = [
            url,
            'apiKey=' + self.key,
            'nonce=' + str(nonce),
            'primaryCurrencyCode='+str(primary_currency_code),
            'secondaryCurrencyCode='+str(secondary_currency_code),
            'pageIndex='+str(page_index),
            'pageSize='+str(page_size)
        ]

        signature = self._generate_signature(parameters)

        # Collection order has to be in the same order as parameters
        data = OrderedDict([
            ("apiKey", self.key),
            ("nonce", nonce),
            ("signature", str(signature)),
            ("primaryCurrencyCode", str(primary_currency_code)),
            ("secondaryCurrencyCode", str(secondary_currency_code)),
            ("pageIndex", page_index),
            ("pageSize", page_size)
        ])

        response = requests.post(url, data=json.dumps(data, sort_keys=False), headers=self.headers)

        return response
