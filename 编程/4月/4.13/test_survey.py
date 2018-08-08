__author__ = "Narwhale"
# import unittest
# from survey import AnonymousSurvey
#
# class TestAnonymousSurvey(unittest.TestCase):
#     '''测试survey.py'''
#     def test_store_single_response(self):
#         '''测试单个答案会不会妥善储存'''
#         question =  "What langage did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('English')
#         self.assertIn('English',my_survey.responses)
#
#     def test_store_three_response(self):
#         '''测试三个答案会不会妥善储存'''
#         question = "What langage did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         responses = ['English','Spanish','Mandarin']
#         for response in responses:
#             my_survey.store_response(response)
#         for response in responses:
#             self.assertIn(response,my_survey.responses)
#

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''测试survey.py'''

    def setUp(self):
        '''创建一个调查对象和一答案，供使用的测试方法使用'''
        question = "What langage did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']

    def test_store_single_response(self):
        '''测试单个答案会不会妥善储存'''
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_response(self):
        '''测试三个答案会不会妥善储存'''
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

