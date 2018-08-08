__author__ = "Narwhale"

# from survey import AnonymousSurvey
#
# question = "What language did you first learn to speak?"
# my_survey = AnonymousSurvey(question)
#
# my_survey.show_question()
# print("Enter 'q' at any time to quit .\n")
# while True:
#     response = input('Langage:')
#     if response == 'q':
#         break
#     my_survey.stor_response(response)
# print("\nTank you to everyone who participated in the servey!")
# my_survey.show_results()

from survey import AnonymousSurvey

question = "What langage did you first learn to speak?"
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:

    response = input('Langage:')
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nTank you to everyone who participated in the servey!")
my_survey.show_results()