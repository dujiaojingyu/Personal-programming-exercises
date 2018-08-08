__author__ = "Narwhale"
#
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.strip())
s = ''
with open('pi_digits.txt') as file_object:
    for line in file_object:
        s += line.strip()
    print(s)