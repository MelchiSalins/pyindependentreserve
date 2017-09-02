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
    def place_limit_order(self, price, volume, primary_currency_code="Xbt",
                          secondary_currency_code="Aud", order_type="LimitBid"):
        """

        :param price: The price in secondary currency to buy/sell.
        :param volume: The volume to buy/sell in primary currency.
        :param primary_currency_code: The digital currency code of limit order. Must be a valid primary currency,
                                      which can be checked via the GetValidPrimaryCurrencyCodes method.
        :param secondary_currency_code: The fiat currency of limit order. Must be a valid secondary currency,
                                        which can be checked via the GetValidSecondaryCurrencyCodes method.
        :param order_type: The type of limit order. Must be a valid limit order type,
                           which can be checked via the GetValidLimitOrderTypes method.
        :return:


        {
            "apiKey":"{api-key}",
            "nonce":{nonce},
            "signature":"{signature}",
            "primaryCurrencyCode":"Xbt",
            "secondaryCurrencyCode":"Usd",
            "orderType": "LimitBid",
            "price": 485.76,
            "volume": 0.358
        }

        {
            "CreatedTimestampUtc":"2014-08-05T06:42:11.3032208Z",
            "OrderGuid":"719c495c-a39e-4884-93ac-280b37245037",
            "Price":485.76,
            "PrimaryCurrencyCode":"Xbt",
            "ReservedAmount":0.358,
            "SecondaryCurrencyCode":"Usd",
            "Status":"Open",
            "Type":"LimitOffer",
            "VolumeFilled":0,
            "VolumeOrdered":0.358
        }
        """
        nonce = int(time.time())
        url = "https://api.independentreserve.com/Private/PlaceLimitOrder"

        parameters = [
            url,
            'apiKey=' + self.key,
            'nonce=' + str(nonce),
            'primaryCurrencyCode=' + str(primary_currency_code),
            'secondaryCurrencyCode=' + str(secondary_currency_code),
            'orderType=' + str(order_type),
            'price=' + str(price),
            'volume=' + str(volume)
        ]

        signature = self._generate_signature(parameters)

        # Collection order has to be in the same order as parameters
        data = OrderedDict([
            ("apiKey", self.key),
            ("nonce", nonce),
            ("signature", str(signature)),
            ("primaryCurrencyCode", str(primary_currency_code)),
            ("secondaryCurrencyCode", str(secondary_currency_code)),
            ("orderType", order_type),
            ("price", price),
            ("volume", volume)
        ])

        response = requests.post(url, data=json.dumps(data, sort_keys=False), headers=self.headers)

        return response

    @http_exception_handler
    def place_market_order(self, volume, primary_currency_code="Xbt", secondary_currency_code="Aud", order_type="MarketBid"):
        """
        Place new market bid / offer order. A Market Bid is a buy order and a Market Offer is a sell order.

        :param volume: The volume to buy/sell in primary currency.
        :param primary_currency_code: The digital currency code of market order. Must be a valid primary currency,
                                      which can be checked via the GetValidPrimaryCurrencyCodes method.
        :param secondary_currency_code: The fiat currency of market order. Must be a valid secondary currency,
                                        which can be checked via the GetValidSecondaryCurrencyCodes method.
        :param order_type: The type of market order. Must be a valid market order type,
                           which can be checked via the GetValidMarketOrderTypes method.
        :return: dict

        {
            "CreatedTimestampUtc":"2014-08-05T06:42:11.3032208Z",
            "OrderGuid":"5c8885cd-5384-4e05-b397-9f5119353e10",
            "PrimaryCurrencyCode":"Xbt",
            "ReservedAmount":0.025,
            "SecondaryCurrencyCode":"Usd",
            "Status":"Open",
            "Type":"MarketOffer",
            "VolumeFilled":0,
            "VolumeOrdered":0.025
        }
        """
        nonce = int(time.time())
        url = "https://api.independentreserve.com/Private/PlaceMarketOrder"

        parameters = [
            url,
            'apiKey=' + self.key,
            'nonce=' + str(nonce),
            'primaryCurrencyCode=' + str(primary_currency_code)
            'secondaryCurrencyCode=' + str(secondary_currency_code),
            'orderType=' + str(order_type),
            'volume=' + str(volume)
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict([
            ("apiKey", self.key),
            ("nonce", nonce),
            ("signature", str(signature)),
            ("primaryCurrencyCode", str(primary_currency_code)),
            ("secondaryCurrencyCode", str(secondary_currency_code)),
            ("orderType", order_type),
            ("volume", volume)
        ])

        response = requests.post(url, data=json.dumps(data, sort_keys=False), headers=self.headers)

        return response


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
