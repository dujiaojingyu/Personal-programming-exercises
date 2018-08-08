__author__ = "Narwhale"

class Restaurant(object):
    '''餐厅类'''
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''餐厅的详细'''
        masg = self.restaurant_name + ' serves wonderful ' + self.cuisine_type
        print('\n',masg)
    def open_restaurant(self):
        '''餐厅营业中'''
        masg = self.restaurant_name + " is open. Come on in!"
        print('\n',masg)



# A = Restaurant('A','pizza')
#
# A.describe_restaurant()
# A.open_restaurant()
#


class IceCreamStand(Restaurant):
    '''冰淇凌餐厅'''
    def __init__(self,restaurant_name,cuisine_type='ice_cream'):
        super(IceCreamStand, self).__init__(restaurant_name,cuisine_type)
        self.flavors = []
    def show_flavors(self):
        '''打印喜欢的冰淇凌'''
        print("\nWe have the following flavors available:")
        for i in self.flavors:
            print(' -',i.title())

B = IceCreamStand('The Big One')
B.flavors = ['vanilla', 'chocolate', 'black cherry']

B.open_restaurant()
B.describe_restaurant()

B.show_flavors()