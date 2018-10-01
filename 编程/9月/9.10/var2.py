__author__ = "Narwhale"

# with open('info.txt','w',encoding='utf-8') as f:
#     f.write('500')
# s = ''
# with open('info.txt','r',encoding='utf-8') as f:
#     for l in f:
#         l = l.strip()
#         s = s + ''.join(l)
#     print(len(s[:11]))

###########################################
import sys
import string
s = str(help(string))
with open('string_help.txt','w',encoding='utf-8') as f:
    # for line in help(string):
    #     line = line
    #     f.write(line)
    sys.stdout = f
    help(string)


#############################

# import sys
#
# a = '1234'
# print(id(a))
# print(sys.getrefcount('1234'))
# b = a
# print(sys.getrefcount('1234'))
# c = a
# print(sys.getrefcount('1234'))
