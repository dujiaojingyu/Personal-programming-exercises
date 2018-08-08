__author__ = "Narwhale"

import configparser

config = configparser.ConfigParser()
config.read('example.ini')

print(config.sections())
print(config.default_section)
print(config.defaults())