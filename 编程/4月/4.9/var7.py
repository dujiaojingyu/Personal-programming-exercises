__author__ = "Narwhale"

cities = {
    'guangzhou':{
        'country':'China',
        'population':'10000000',
        'fact':'First-tier cities'
    },

    'shenzhen':{
        'country': 'China',
        'population': '8000000',
        'fact': 'First-tier cities'
    },
    'foshan':{
        'country': 'China',
        'population': '6000000',
        'fact': 'second-tier cities'
    },
}

for place,infomation in cities.items():
    print(place+':')
    for i,f in infomation.items():
        print('\t',i,end=':')
        print(f)
