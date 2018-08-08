for each in range(100,999):
    g = each % 10
    s = (each//10) % 10
    b = (each//100) % 10
    result = g**3 + s**3 + b**3
    if result == each:
        print(each)