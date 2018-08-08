__author__ = "Narwhale"

import string

s = string.ascii_lowercase

def alphabet_position(text):
    string_l = []
    t = text.split()
    for j in t:
        t = "".join(t)
    for i in t:

        if i.lower() in s:
            result = s.index(i.lower()) + 1
            string_l.append(str(result))
    date_str = " ".join(string_l)

    return date_str

print(alphabet_position("The sunset sets at twelve o' clock."))