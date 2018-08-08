__author__ = "Narwhale"

class AnonymousSurvey():
    '''收集匿名调查问卷'''

    def __init__(self,question):
        '''存储一个问题，并为其存储答案准备'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''显示调查问卷'''
        print(self.question)

    def store_response(self,new_response):
        '''存储单份答案'''
        self.responses.append(new_response)

    def show_results(self):
        '''显示答案'''
        print('Survey results:')
        for response in self.responses:
            print('- ',response)

# class AnonymousSurvey():
#     '''收集匿名调查问卷'''
#     def __init__(self,question):
#         '''存储一个问题，并为其存储回答'''
#         self.question = question
#         self.responses = []
#
#
#     def show_question(self):
#         '''显示调查问卷题目'''
#         print(self.question)
#
#     def store_response(self,new_response):
#         '''存储回答'''
#         self.responses.append(new_response)
#
#     def show_results(self):
#         '''显示调查问卷回答'''
#         print('Survey results:')
#         for response in self.responses:
#             print('- ',response)