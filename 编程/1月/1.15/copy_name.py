name = ['hsj','yrq','zc',['shjd','shgdh'],'lgm','frt']
'''name2 = name
print(name)
print(name2)
name2 = name.copy()
name[2] = 'hsk'
print(name)
print(name2)'''
#name2 = name[:]
#name2 = name[0:-1]
#name[3] = 'hsk'
#print(name)
#print(name2)
import copy
name2 = copy.deepcopy(name)
name[3][0] = 'hsk'
print(name)
print(name2)