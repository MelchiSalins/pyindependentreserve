import json
import time
from datetime import datetime

import requests

from collections import OrderedDict

from .authentication import Authentication
from .exceptions import http_exception_handler


class PrivateMethods(Authentication):
    def __init__(
        self, api_key, api_secret, api_url="https://api.independentreserve.com"
    ):
        super(PrivateMethods, self).__init__(api_key, api_secret, api_url)

    @http_exception_handler
    def place_limit_order(
        self,
        price,
        volume,
        primary_currency_code="Xbt",
        secondary_currency_code="Aud",
        order_type="LimitBid",
    ):
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
        url = self.url + "/Private/PlaceLimitOrder"

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "primaryCurrencyCode=" + str(primary_currency_code),
            "secondaryCurrencyCode=" + str(secondary_currency_code),
            "orderType=" + str(order_type),
            "price=" + str(price),
            "volume=" + str(volume),
        ]

        signature = self._generate_signature(parameters)

        # Collection order has to be in the same order as parameters
        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("primaryCurrencyCode", str(primary_currency_code)),
                ("secondaryCurrencyCode", str(secondary_currency_code)),
                ("orderType", order_type),
                ("price", price),
                ("volume", volume),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def place_market_order(
        self,
        volume,
        primary_currency_code="Xbt",
        secondary_currency_code="Aud",
        order_type="MarketBid",
    ):
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
        url = self.url + "/Private/PlaceMarketOrder"

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "primaryCurrencyCode=" + str(primary_currency_code),
            "secondaryCurrencyCode=" + str(secondary_currency_code),
            "orderType=" + str(order_type),
            "volume=" + str(volume),
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("primaryCurrencyCode", str(primary_currency_code)),
                ("secondaryCurrencyCode", str(secondary_currency_code)),
                ("orderType", order_type),
                ("volume", volume),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def cancel_order(self, order_guid):
        """
        Cancels a previously placed order.

        Notes

        The order must be in either 'Open' or 'PartiallyFilled' status to be valid for cancellation.
        You can retrieve list of Open and Partially Filled orders via the GetOpenOrders method.
        You can also check an individual order's status by calling the GetOrderDetails method.

        :param order_guid: The guid of currently open or partially filled order.
        :return: dict

        {
            "CreatedTimestampUtc":"2014-08-05T06:42:11.3032208Z",
            "OrderGuid":"719c495c-a39e-4884-93ac-280b37245037",
            "Price":485.76,
            "PrimaryCurrencyCode":"Xbt",
            "ReservedAmount":0.358,
            "SecondaryCurrencyCode":"Usd",
            "Status":"Cancelled",
            "Type":"LimitOffer",
            "VolumeFilled":0,
            "VolumeOrdered":0.358
        }
        """

        nonce = int(time.time())
        url = self.url + "/Private/CancelOrder"

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "orderGuid=" + str(order_guid),
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("orderGuid", str(order_guid)),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def get_open_orders(
        self,
        primary_currency_code="Xbt",
        secondary_currency_code="Aud",
        page_index=1,
        page_size=10,
    ):
        """
        Retrieves a page of a specified size, with your currently Open and Partially Filled orders.
        :return:
        """

        nonce = int(time.time())
        url = self.url + "/Private/GetOpenOrders"

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "primaryCurrencyCode=" + str(primary_currency_code),
            "secondaryCurrencyCode=" + str(secondary_currency_code),
            "pageIndex=" + str(page_index),
            "pageSize=" + str(page_size),
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("primaryCurrencyCode", str(primary_currency_code)),
                ("secondaryCurrencyCode", str(secondary_currency_code)),
                ("pageIndex", page_index),
                ("pageSize", page_size),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def get_closed_orders(
        self,
        primary_currency_code="Xbt",
        secondary_currency_code="Aud",
        page_index=1,
        page_size=50,
    ):
        """

        :param primary_currency_code: The primary currency of orders. This is an optional parameter.
        :param secondary_currency_code: The secondary currency of orders. This is an optional parameter.
        :param page_index: The page index. Must be greater or equal to 1
        :param page_size: Must be greater or equal to 1 and less than or equal to 50.
                          If a number greater than 50 is specified, then 50 will be used.
        :return: dict

        "PageSize": Number of orders shown per page
        "TotalItems": Total number of closed orders
        "TotalPages": Total number of pages
        "Data":[ List of all open orders
        {
            "AvgPrice": Average price for all trades executed for the order
            "CreatedTimestampUtc": UTC timestamp of when order was created
            "FeePercent": Brokerage fee
            "OrderGuid": Unique identifier of the order
            "OrderType": Type of order,
            "Outstanding": Unfilled volume still outstanding on this order
            "Price": Order limit price in secondary currency
            "PrimaryCurrencyCode": Primary currency of order
            "SecondaryCurrencyCode": Secondary currency of order
            "Status": Order status (Filled, PartiallyFilledAndCancelled, Cancelled, PartiallyFilledAndExpired, Expired)
            "Value": The value of the order, denominated in secondary currency
            "Volume": The original volume ordered
        }]
        """
        nonce = int(time.time())
        url = self.url + "/Private/GetClosedOrders"

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "primaryCurrencyCode=" + str(primary_currency_code),
            "secondaryCurrencyCode=" + str(secondary_currency_code),
            "pageIndex=" + str(page_index),
            "pageSize=" + str(page_size),
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("primaryCurrencyCode", str(primary_currency_code)),
                ("secondaryCurrencyCode", str(secondary_currency_code)),
                ("pageIndex", page_index),
                ("pageSize", page_size),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def get_closed_filled_orders(
        self,
        primary_currency_code="Xbt",
        secondary_currency_code="Aud",
        page_index=1,
        page_size=50,
    ):
        """

        :param primary_currency_code: The primary currency of orders. This is an optional parameter.
        :param secondary_currency_code: The secondary currency of orders. This is an optional parameter.
        :param page_index: The page index. Must be greater or equal to 1
        :param page_size: Must be greater or equal to 1 and less than or equal to 50.
                          If a number greater than 50 is specified, then 50 will be used.
        :return: dict

        "PageSize": Number of orders shown per page
        "TotalItems": Total number of closed orders
        "TotalPages": Total number of pages
        "Data":[ List of all open orders
        {
            "AvgPrice": Average price for all trades executed for the order
            "CreatedTimestampUtc": UTC timestamp of when order was created
            "FeePercent": Brokerage fee
            "OrderGuid": Unique identifier of the order
            "OrderType": Type of order,
            "Outstanding": Unfilled volume still outstanding on this order
            "Price": Order limit price in secondary currency
            "PrimaryCurrencyCode": Primary currency of order
            "SecondaryCurrencyCode": Secondary currency of order
            "Status": Order status (Filled, PartiallyFilledAndCancelled, PartiallyFilledAndExpired)
            "Value": The value of the order, denominated in secondary currency
            "Volume": The original volume ordered
        }]
        """
        nonce = int(time.time())
        url = self.url + "/Private/GetClosedFilledOrders"

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "primaryCurrencyCode=" + str(primary_currency_code),
            "secondaryCurrencyCode=" + str(secondary_currency_code),
            "pageIndex=" + str(page_index),
            "pageSize=" + str(page_size),
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("primaryCurrencyCode", str(primary_currency_code)),
                ("secondaryCurrencyCode", str(secondary_currency_code)),
                ("pageIndex", page_index),
                ("pageSize", page_size),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def get_order_details(self, order_guid):
        """
        Retrieves details about a single order.

        :param order_guid:The guid of the order.
        :return: dict

        {
          "OrderGuid": "c7347e4c-b865-4c94-8f74-d934d4b0b177",
          "CreatedTimestampUtc": "2014-09-23T12:39:34.3817763Z",
          "Type": "MarketBid",
          "VolumeOrdered": 5.0,
          "VolumeFilled": 5.0,
          "Price": null,
          "AvgPrice": 100.0,
          "ReservedAmount": 0.0,
          "Status": "Filled",
          "PrimaryCurrencyCode": "Xbt",
          "SecondaryCurrencyCode": "Usd"
        }
        """
        nonce = int(time.time())
        url = self.url + "/Private/GetOrderDetails"

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "orderGuid=" + str(order_guid),
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("orderGuid", str(order_guid)),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def get_accounts(self):
        """
        Retrieves information about your Independent Reserve accounts in digital and fiat currencies.

        :return: list

        [
            {
                "AccountGuid":"66dcac65-bf07-4e68-ad46-838f51100424",
                "AccountStatus":"Active",
                "AvailableBalance":45.33400000,
                "CurrencyCode":"Xbt",
                "TotalBalance":46.81000000
            },
            {
                "AccountGuid":"49994921-60ec-411e-8a78-d0eba078d5e9",
                "AccountStatus":"Active",
                "AvailableBalance":14345.53000000,
                "CurrencyCode":"Usd",
                "TotalBalance":15784.07000000
            }
        ]
        """
        nonce = int(time.time())
        url = self.url + "/Private/GetAccounts"

        parameters = [url, "apiKey=" + self.key, "nonce=" + str(nonce)]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def get_transactions(
        self,
        account_guid,
        from_date=datetime(1970, 1, 1),
        to_date=datetime(1970, 1, 1),
        transaction_types="",
        page_index=1,
        page_size=50,
    ):
        """

        Retrieves a page of a specified size, containing all trnasactions made on an account.

        :param account_guid: The Guid of your Independent Reseve account.
                             You can retrieve information about your accounts via the GetAccounts method.
        :param from_date: The optional start date (UTC) to retrieve transactions.
        :param to_date: The optional end date (UTC) to retrieve transactions.
        :param transaction_types: The optional list of transaction types to filter result.
        :param page_index: The page index. Must be greater or equal to 1
        :param page_size: Must be greater or equal to 1 and less than or equal to 50.
                          If a number greater than 50 is specified, then 50 will be used.
        :return:
        """
        nonce = int(time.time())
        url = self.url + "/Private/GetTransactions"

        fromTimestampUtc = ""
        if from_date != None:
            fromTimestampUtc = from_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        toTimestampUtc = ""
        if to_date != None:
            toTimestampUtc = to_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        txTypes = ""
        txTypesData = ""
        if transaction_types != None:
            txTypes = ",".join(transaction_types)
            txTypesData = transaction_types

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "accountGuid=" + str(account_guid),
            "fromTimestampUtc=" + fromTimestampUtc,
            "toTimestampUtc=" + toTimestampUtc,
            "txTypes=" + txTypes,
            "pageIndex=" + str(page_index),
            "pageSize=" + str(page_size),
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("accountGuid", account_guid),
                ("fromTimestampUtc", fromTimestampUtc),
                ("toTimestampUtc", toTimestampUtc),
                ("txTypes", txTypesData),
                ("pageIndex", page_index),
                ("pageSize", page_size),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def get_digital_currency_deposit_address(self, primary_currency_code="Xbt"):
        """
        Retrieves the deposit address which should be used for new Bitcoin or Ether deposits.

        :param primary_currency_code: The digital currency to generate deposit address for.
        :return: dict

        {
            "DepositAddress":"12a7FbBzSGvJd36wNesAxAksLXMWm4oLUJ",
            "LastCheckedTimestampUtc":"2014-05-05T09:35:22.4032405Z",
            "NextUpdateTimestampUtc":"2014-05-05T09:45:22.4032405Z"
        }
        """
        nonce = int(time.time())
        url = self.url + "/Private/GetDigitalCurrencyDepositAddress"

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "primaryCurrencyCode=" + str(primary_currency_code),
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("primaryCurrencyCode", str(primary_currency_code)),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def get_digital_currency_deposit_addresses(
        self, primary_currency_code="Xbt", page_index=1, page_size=50
    ):
        """
        Retrieves a page of digital currency deposit addresses which have been assigned to your account.

        :param primary_currency_code: The digital currency to generate deposit address for.
        :param page_index: The page index. Must be greater or equal to 1
        :param page_size: Must be greater or equal to 1 and less than or equal to 50.
                          If a number greater than 50 is specified, then 50 will be used.
        :return: dict

        {
            "PageSize": 10,
            "TotalItems": 10,
            "TotalPages": 1
            "Data": [
                    {
                        "DepositAddress": "1CxrjaGvVLgXwi1s1d9d62hrCVLU83nHpX",
                        "LastCheckedTimestampUtc": "2014-07-24T11:23:48.8693053Z",
                        "NextUpdateTimestampUtc": "2014-07-25T11:23:48.8693053Z"
                    },
                    // ...
                    {
                        "DepositAddress":"12a7FbBzSGvJd36wNesAxAksLXMWm4oLUJ",
                        "LastCheckedTimestampUtc":"2014-05-05T09:35:22.4032405Z",
                        "NextUpdateTimestampUtc":"2014-05-05T09:45:22.4032405Z"
                    }
            ]
        }
        """
        nonce = int(time.time())
        url = self.url + "/Private/GetDigitalCurrencyDepositAddresses"

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "primaryCurrencyCode=" + str(primary_currency_code),
            "pageIndex=" + str(page_index),
            "pageSize=" + str(page_size),
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("primaryCurrencyCode", str(primary_currency_code)),
                ("pageIndex", str(page_index)),
                ("pageSize", str(page_size)),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def synch_digital_currency_deposit_address_with_blockchain(self, deposit_address):
        """
        Forces the deposit address to be checked for new Bitcoin or Ether deposits.

        :param deposit_address: Bitcoin or Ether deposit address to check for new deposits.
        :return: dict

        {
            "DepositAddress":"12a7FbBzSGvJd36wNesAxAksLXMWm4oLUJ",
            "LastCheckedTimestampUtc":"2014-05-05T09:35:22.4032405Z",
            "NextUpdateTimestampUtc":"2014-05-05T09:45:22.4032405Z"
        }
        """
        nonce = int(time.time())
        url = self.url + "/Private/SynchDigitalCurrencyDepositAddressWithBlockchain"

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "depositAddress=" + str(deposit_address),
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("depositAddress", str(deposit_address)),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def withdraw_digital_currency(self, amount, withdrawal_address, comment=""):
        """
        Creates a digital currency withdrawal request. There is a minimum withdrawal amount of XBT 0.001 or ETH 0.01,
        except where the available balance is less than this amount. In all cases, the withdrawal amount must be greater
        than the withdrawal fee. Take care to provide a valid destination address.
        Bitcoin and Ether withdrawals are irreversible once sent.


        :param amount: The amount of Bitcoin to withdraw.
        :param withdrawal_address: Target Bitcoin or Ether withdrawal address.
        :param comment: Withdrawal comment. Should not exceed 500 characters.
        :return: null
        """
        nonce = int(time.time())
        url = self.url + "/Private/WithdrawDigitalCurrency"

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "amount=" + str(amount),
            "withdrawalAddress=" + str(withdrawal_address),
            "comment=" + str(comment),
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("amount", str(amount)),
                ("withdrawalAddress", str(withdrawal_address)),
                ("comment", str(comment)),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def request_fiat_withdrawal(
        self,
        withdrawal_amount,
        withdrawal_bank_account_name,
        secondary_currency_code="USD",
        comment="",
    ):
        nonce = int(time.time())
        url = self.url + "/Private/RequestFiatWithdrawal"

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "secondaryCurrencyCode=" + str(secondary_currency_code),
            "withdrawalAmount=" + str(withdrawal_amount),
            "withdrawalBankAccountName=" + str(withdrawal_bank_account_name),
            "comment=" + str(comment),
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("secondaryCurrencyCode", str(secondary_currency_code)),
                ("withdrawalAmount", str(withdrawal_amount)),
                ("withdrawalBankAccountName", str(withdrawal_bank_account_name)),
                ("comment", str(comment)),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def get_trades(self, page_index=1, page_size=50):
        """
        Retrieves a page of a specified size, containing trades which were executed against your orders.

        :param page_index: The page index. Must be greater or equal to 1
        :param page_size: Must be greater or equal to 1 and less than or equal to 50.
                          If a number greater than 50 is specified, then 50 will be used.
        :return:

        {
          "Data": [
            {
              "TradeGuid": "593e609d-041a-4f46-a41d-2cb8e908973f",
              "TradeTimestampUtc": "2014-12-16T03:44:19.2187707Z",
              "OrderGuid": "8bf851a3-76d2-439c-945a-93367541d467",
              "OrderType": "LimitBid",
              "OrderTimestampUtc": "2014-12-16T03:43:36.7423769Z",
              "VolumeTraded": 0.5,
              "Price": 410.0,
              "PrimaryCurrencyCode": "Xbt",
              "SecondaryCurrencyCode": "Usd"
            },
            // ...
            {
              "TradeGuid": "13c1e71c-bfb4-452c-b13e-e03535f98b09",
              "TradeTimestampUtc": "2014-12-11T11:37:42.2089564Z",
              "OrderGuid": "1ce88acf-6013-4867-b58d-77f0e41ec475",
              "OrderType": "LimitBid",
              "OrderTimestampUtc": "2014-12-11T11:37:42.0724391Z",
              "VolumeTraded": 0.4,
              "Price": 399.0,
              "PrimaryCurrencyCode": "Xbt",
              "SecondaryCurrencyCode": "Usd"
            }
          ],
          "PageSize": 5,
          "TotalItems": 20,
          "TotalPages": 4
        }
        """
        nonce = int(time.time())
        url = self.url + "/Private/GetTrades"

        parameters = [
            url,
            "apiKey=" + self.key,
            "nonce=" + str(nonce),
            "pageIndex=" + str(page_index),
            "pageSize=" + str(page_size),
        ]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [
                ("apiKey", self.key),
                ("nonce", nonce),
                ("signature", str(signature)),
                ("pageIndex", page_index),
                ("pageSize", page_size),
            ]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response

    @http_exception_handler
    def get_brokerage_fees(self):
        """
        Retrieves information about the trading fees for the digital currencies in your Independent Reserve account.

        :return:

        [
          {
            "CurrencyCode": "Xbt",
            "Fee": 0.005
          },
          {
            "CurrencyCode": "Eth",
            "Fee": 0.005
          },
          {
            "CurrencyCode": "Bch",
            "Fee": 0.014
          }
        ]
        """
        nonce = int(time.time())
        url = self.url + "/Private/GetBrokerageFees"

        parameters = [url, "apiKey=" + self.key, "nonce=" + str(nonce)]

        signature = self._generate_signature(parameters)

        data = OrderedDict(
            [("apiKey", self.key), ("nonce", nonce), ("signature", str(signature))]
        )

        response = requests.post(
            url, data=json.dumps(data, sort_keys=False), headers=self.headers
        )

        return response
