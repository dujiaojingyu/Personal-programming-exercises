__author__ = "Narwhale"

# def city_country_formatted(city,country,population):
#     '''格式化城市和国家'''
#     result = city + ',' + country
#     result = result.title()
#     print(result)
#     full_result = result + ' - population ' + str(population)
#     print(full_result)
#     return full_result



def city_country_formatted(city,country,population=0):
    '''格式化城市和国家'''
    full_result =city.title() + ',' + country.title()
    if population:
        full_result = full_result + ' - population ' + str(population)
    return full_result