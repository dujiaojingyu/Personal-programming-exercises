__author__ = "Narwhale"
# import unittest
# from city_functions import city_country_formatted
#
# class CityCountryTestCase(unittest.TestCase):
#     '''测试city_functions.py'''
#     def test_city_country_formatted(self):
#         formatted_city_country = city_country_formatted('santiago','chile',population=5000000)
#         self.assertEqual(formatted_city_country,'Santiago,Chile - population 5000000')



import unittest
from city_functions import city_country_formatted

class CityCountryTestCase(unittest.TestCase):
    '''测试city_functions.py'''
    def test_city_country_formatted(self):
        formatted_city_country = city_country_formatted('santiago','chile')
        self.assertEqual(formatted_city_country,'Santiago,Chile')

    def test_city_country_population(self):
        '''Can I include a population argument?'''
        formatted_city_country = city_country_formatted('santiago','chile',population=5000000)
        self.assertEqual(formatted_city_country,'Santiago,Chile - population 5000000')