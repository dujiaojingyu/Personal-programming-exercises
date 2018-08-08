__author__ = "Narwhale"

# def get_formatted_name(first,last):
#     '''合并姓名'''
#     full_name = first + ' ' + last
#     return full_name.title()
#




#------------------------------------------------------


def get_formatted_name(first,last,moddle=''):
    '''合并姓名'''
    if moddle:
        full_name = first + ' ' + moddle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()