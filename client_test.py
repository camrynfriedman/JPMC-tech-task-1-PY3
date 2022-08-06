import unittest
from client3 import *

# Edited by Camryn Friedman 8/5/22


class ClientTest(unittest.TestCase):

    # Test getDataPoint generic
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'],
                                                   quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))

    # Test getDataPoint with bid > ask
    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'],
                                                   quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))

    """ ------------ Add more unit tests ------------ """

    # Test getRatio generic
    def test_getRatio_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = {}
        i = 0
        for quote in quotes:
            prices[i] = (quote['top_ask']['price'] +
                         quote['top_bid']['price'])/2
            i += 1
        self.assertEqual(
            getRatio(prices[0], prices[1]), prices[0]/prices[1])

    # Test getRatio with price_a = 0
    def test_getRatio_calculatePriceAisZero(self):
        quotes = [
            {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = {}
        i = 0
        for quote in quotes:
            prices[i] = (quote['top_ask']['price'] +
                         quote['top_bid']['price'])/2
            i += 1
        self.assertEqual(
            getRatio(prices[0], prices[1]), prices[0]/prices[1])

    # Test getRatio with price_b = 0
    def test_getRatio_calculatePriceBisZero(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = {}
        i = 0
        for quote in quotes:
            prices[i] = (quote['top_ask']['price'] +
                         quote['top_bid']['price'])/2
            i += 1
        self.assertEqual(
            getRatio(prices[0], prices[1]), None)


if __name__ == '__main__':
    unittest.main()
