import requests
import logging

from .exceptions import http_exception_handler


class PublicMethods(object):
    """

    """

    def __init__(self):
        pass

    @staticmethod
    @http_exception_handler
    def get_valid_primary_currency_codes():
        """
        Returns a list of valid primary currency codes. These are the digital currencies which can be traded
        on Independent Reserve.

        This method does not take any parameters.

        :return: list
        """
        response = requests.get("https://api.independentreserve.com/Public/GetValidPrimaryCurrencyCodes")
        return response

    @staticmethod
    @http_exception_handler
    def get_valid_secondary_currency_codes():
        """
        Returns a list of valid secondary currency codes. These are the fiat currencies which are supported by
        Independent Reserve for trading purposes.

        :return: list

        ["Usd","Aud", "Nzd"]
        """
        response = requests.get("https://api.independentreserve.com/Public/GetValidSecondaryCurrencyCodes")
        return response

    @staticmethod
    @http_exception_handler
    def get_valid_limit_order_types():
        """
        Returns a list of valid limit order types which can be placed onto the Independent Reserve exchange platform.

        :return: list

        ["LimitBid","LimitOffer"]
        """
        response = requests.get("https://api.independentreserve.com/Public/GetValidLimitOrderTypes")
        return response

    @staticmethod
    @http_exception_handler
    def get_valid_transaction_types():
        """
        Returns a list of valid transaction types.
        This method does not take any parameters.

        :return: list

        [u'Brokerage',
         u'Deposit',
         u'DepositFee',
         u'GST',
         u'ReferralCommission',
         u'Trade',
         u'Withdrawal',
         u'WithdrawalFee']
        """
        response = requests.get("https://api.independentreserve.com/Public/GetValidTransactionTypes")
        return response


    @staticmethod
    @http_exception_handler
    def get_market_summary(primary_currency="Xbt", secondary_currency_code="Aud"):
        """
        Returns a current snapshot of the Independent Reserve market for a given currency pair

        This method caches return values for 1 second. Calling it more than once per second will result in cached data
        being returned.

        :return: dict

        {
           "CreatedTimestampUtc ":"2014-08-05T06:42:11.3032208Z",
           "CurrentHighestBidPrice":500.00000000,
           "CurrentLowestOfferPrice":1001.00000000,
           "DayAvgPrice":510.000000,
           "DayHighestPrice":510.00000000,
           "DayLowestPrice":510.00000000,
           "DayVolumeXbt":1.00000000,
           "DayVolumeXbtInSecondaryCurrrency":0.75000000,
           "LastPrice":510.00000000,
           "PrimaryCurrencyCode":"Xbt",
           "SecondaryCurrencyCode":"Usd"
        }

        Return value description
        "CreatedTimestampUtc ": UTC timestamp of when the market summary was generated
        "CurrentHighestBidPrice": Current highest bid on order book
        "CurrentLowestOfferPrice": Current lowest offer on order book
        "DayAvgPrice": Weighted average traded price over last 24 hours
        "DayHighestPrice": Highest traded price over last 24 hours
        "DayLowestPrice": Lowest traded price over last 24 hours
        "DayVolumeXbt": Volume of primary currency traded in last 24 hours
        "DayVolumeXbtInSecondaryCurrrency": Volume of primary currency traded in last 24 hours for chosen secondary
                                            currency
        "LastPrice": Last traded price
        "PrimaryCurrencyCode": The primary currency being summarised
        "SecondaryCurrencyCode": The secondary currency being used for pricing

        """
        response = requests.get(
            "https://api.independentreserve.com/Public/GetMarketSummary?\
            primaryCurrencyCode={0}&secondaryCurrencyCode={1}".format(primary_currency, secondary_currency_code))
        return response

    @staticmethod
    @http_exception_handler
    def get_order_book(primary_currency="Xbt", secondary_currency="Aud"):
        """
        Returns the Order Book for a given currency pair.

        This method caches return values for 1 second. Calling it more than once per second will result in cached
        data being returned.

        :return: dict

        {
           "BuyOrders":[
              {
                 "OrderType":"LimitBid",
                 "Price":497.02000000,
                 "Volume":0.01000000
              },
              {
                 "OrderType":"LimitBid",
                 "Price":490.00000000,
                 "Volume":1.00000000
              }
           ],
           "CreatedTimestampUtc ":"2014-08-05T06:42:11.3032208Z",
           "PrimaryCurrencyCode":"Xbt",
           "SecondaryCurrencyCode":"Usd",
           "SellOrders":[
              {
                 "OrderType":"LimitOffer",
                 "Price":500.00000000,
                 "Volume":1.00000000
              },
              {
                 "OrderType":"LimitOffer",
                 "Price":505.00000000,
                 "Volume":1.00000000
              }
           ]
        }
        """
        response = requests.get(
            "https://api.independentreserve.com/Public/GetOrderBook?\
            primaryCurrencyCode={0}&secondaryCurrencyCode={1}".format(primary_currency, secondary_currency))
        return response
