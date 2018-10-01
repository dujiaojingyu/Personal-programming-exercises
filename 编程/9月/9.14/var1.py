__author__ = "Narwhale"

def gethelpmod(*args):
    c = args[0]
    helpmod = __import__(c)
    print(help(helpmod))
    return help(helpmod)

h = gethelpmod('time')