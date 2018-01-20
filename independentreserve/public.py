"""
Python wrapper for API endpoint documented at https://www.independentreserve.com/API#public
"""

import requests

from .exceptions import http_exception_handler


class PublicMethods(object):
    """
    Python wrapper for API endpoint documented at https://www.independentreserve.com/API#public
    """
    
    """
    Independent Reserve API Url.
    Can override this for testing purposes.
    """
    api_url = "https://api.independentreserve.com"

    def __init__(self, api_url = "https://api.independentreserve.com"):
        PublicMethods.api_url = api_url
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
        response = requests.get(PublicMethods.api_url + "/Public/GetValidPrimaryCurrencyCodes")
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
        response = requests.get(PublicMethods.api_url + "/Public/GetValidSecondaryCurrencyCodes")
        return response

    @staticmethod
    @http_exception_handler
    def get_valid_limit_order_types():
        """
        Returns a list of valid limit order types which can be placed onto the Independent Reserve exchange platform.

        :return: list

        ["LimitBid","LimitOffer"]
        """
        response = requests.get(PublicMethods.api_url + "/Public/GetValidLimitOrderTypes")
        return response

    @staticmethod
    @http_exception_handler
    def get_valid_market_order_types():
        """
        Returns a list of valid market order types which can be placed onto the Independent Reserve exchange platform.

        :return: list

        ["MarketBid","MarketOffer"]
        """
        response = requests.get(PublicMethods.api_url + "/Public/GetValidMarketOrderTypes")
        return response
        
    @staticmethod
    @http_exception_handler
    def get_valid_order_types():
        """
        Returns a list of valid order types which can be placed onto the Independent Reserve exchange platform.

        :return: list

        ["LimitBid","LimitOffer","MarketBid","MarketOffer"]
        """
        response = requests.get(PublicMethods.api_url + "/Public/GetValidOrderTypes")
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
        response = requests.get(PublicMethods.api_url + "/Public/GetValidTransactionTypes")
        return response

    @staticmethod
    @http_exception_handler
    def get_market_summary(primary_currency_code="Xbt", secondary_currency_code="Aud"):
        """
        Returns a current snapshot of the Independent Reserve market for a given currency pair

        This method caches return values for 1 second. Calling it more than once per second will result in cached data
        being returned.

        :param primary_currency_code: Should be of valid code returned by get_valid_primary_currency_code()
        :param secondary_currency_code: Should be of valid code returned by get_valid_secondary_currency_code()
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
            PublicMethods.api_url + "/Public/GetMarketSummary?primaryCurrencyCode={0}&secondaryCurrencyCode={1}".format(
                primary_currency_code, secondary_currency_code))
        return response

    @staticmethod
    @http_exception_handler
    def get_order_book(primary_currency_code="Xbt", secondary_currency_code="Aud"):
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
            PublicMethods.api_url + "/Public/GetOrderBook?primaryCurrencyCode={0}&secondaryCurrencyCode={1}"
                .format(primary_currency_code, secondary_currency_code))
        return response

    @staticmethod
    @http_exception_handler
    def get_trade_history_summary(primary_currency_code="Xbt", secondary_currency_code="Aud", hours="240"):
        """
        Returns summarised historical trading data for a given currency pair. Data is summarised into 1 hour intervals.

        :param primary_currency_code: The digital currency for which to retrieve trade history.
                                      Must be a valid primary currency, which can be checked via the
                                      GetValidPrimaryCurrencyCodes method.
        :param secondary_currency_code: The fiat currency in which to retrieve trade history.

                                        Must be a valid secondary currency, which can be checked via the
                                        GetValidSecondaryCurrencyCodes method.
        :param hours: The time period in hours to get trade history.
        :return: dict

        Notes

        This method caches return values for 30 minutes. Calling it more than once per 30 minutes will result in cached
        data being returned.

        {
           "CreatedTimestampUtc ":"2014-08-05T09:02:57.5440691Z",
           "HistorySummaryItems":[{
                "AverageSecondaryCurrencyPrice":510.00000000,
                "ClosingSecondaryCurrencyPrice":510.00000000,
                "StartTimestampUtc":"2014-08-04T09:00:00Z"
                "EndTimestampUtc":"2014-08-04T10:00:00Z",
                "HighestSecondaryCurrencyPrice":510.00000000,
                "LowestSecondaryCurrencyPrice":510.00000000,
                "NumberOfTrades":0,
                "OpeningSecondaryCurrencyPrice":510.00000000,
                "PrimaryCurrencyVolume":0.00000000,
                "SecondaryCurrencyVolume":0.00000000,
            }],
           "NumberOfHoursInThePastToRetrieve":1,
           "PrimaryCurrencyCode":"Xbt",
           "SecondaryCurrencyCode":"Usd"
        }

        Return value descriptions

        "CreatedTimestampUtc ":UTC timestamp of when the data was generated,
        "HistorySummaryItems":[ List of hourly summary blocks
        {
            "AverageSecondaryCurrencyPrice": Average traded price during hour
            "ClosingSecondaryCurrencyPrice": Last traded price in hour
            "StartTimestampUtc": UTC Start time of hour
            "EndTimestampUtc": UTC End time of hour
            "HighestSecondaryCurrencyPrice": Highest traded price during hour
            "LowestSecondaryCurrencyPrice": Lowest traded price during hour
            "NumberOfTrades":Number of trades executed during hour
            "OpeningSecondaryCurrencyPrice": Opening traded price at start of hour
            "PrimaryCurrencyVolume": Volume of primary currency trade during hour
            "SecondaryCurrencyVolume": Volume of secondary currency traded during hour
        }],
        "NumberOfHoursInThePastToRetrieve": Number of past hours being returned,
        "PrimaryCurrencyCode": The primary currency being shown
        "SecondaryCurrencyCode": The secondary currency being used for pricing

        """

        response = requests.get(
            PublicMethods.api_url + "/Public/GetTradeHistorySummary?primaryCurrencyCode={0}&secondaryCurrencyCode={1}&numberOfHoursInThePastToRetrieve={2}".format(
                primary_currency_code, secondary_currency_code, hours)
        )
        return response

    @staticmethod
    @http_exception_handler
    def get_recent_trades(primary_currency_code="Xbt", secondary_currency_code="Aud", number_of_trades=50):
        """

        :param primary_currency_code: The digital currency for which to retrieve recent trades.
                                      Must be a valid primary currency, which can be checked via the
                                      GetValidPrimaryCurrencyCodes method.
        :param secondary_currency_code: The fiat currency in which to retrieve recent trades.
                                        Must be a valid secondary currency, which can be checked via the
                                        GetValidSecondaryCurrencyCodes method.
        :param number_of_trades: How many recent trades to retrieve (maximum is 50)
        :return: dict

        Notes

        This method caches return values for 1 second. Calling it more than once per second will result in cached data
        being returned.

        {
           "CreatedTimestampUtc ":"2014-08-05T09:14:39.4830696Z",
           "PrimaryCurrencyCode":"Xbt",
           "SecondaryCurrencyCode":"Usd",
           "Trades":[
              {
                 "PrimaryCurrencyAmount":1.00000000,
                 "SecondaryCurrencyTradePrice":510.00000000,
                 "TradeTimestampUtc":"2014-07-31T10:34:05.935412Z"
              },
              {
                 "PrimaryCurrencyAmount":0.01000000,
                 "SecondaryCurrencyTradePrice":501.000000,
                 "TradeTimestampUtc":"2014-07-31T10:33:24.8458426Z"
              }
           ]
        }

        Return value descriptions

        "CreatedTimestampUtc ":UTC timestamp of when the data was generated
        "PrimaryCurrencyCode": The primary currency being shown
        "SecondaryCurrencyCode": The secondary currency being used for pricing
        "Trades":[  List of individual trades
        {
            "PrimaryCurrencyAmount": Amount traded in primary currency
            "SecondaryCurrencyTradePrice": Amount traded in secondary currency
            "TradeTimestampUtc": UTC timestamp of trade
        }]

        """

        response = requests.get(
            PublicMethods.api_url + "/Public/GetRecentTrades?primaryCurrencyCode={0}&secondaryCurrencyCode={1}&numberOfRecentTradesToRetrieve={2}".format(
                primary_currency_code, secondary_currency_code, number_of_trades)
        )
        return response

    @staticmethod
    @http_exception_handler
    def get_fx_rates():
        """
        Returns a list of exchange rates used by Independing Reserve when depositing funds or withdrawing funds from
        accounts.

        :return: list
        """
        response = requests.get(PublicMethods.api_url + "/Public/GetFxRates")
        return response