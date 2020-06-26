
from collections import ChainMap
#key value pair
a = {1: 'Jvaa', 2: 'python'}
b= {3: 'Selenium', 4:'Data science'}


a1 = ChainMap(a,b)
print(a1)