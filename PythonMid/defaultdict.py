from collections import defaultdict
d= defaultdict(int)

d[1] = 'habeshaschool'
d[2] = 'java'

print(",,,,,,,,,,," , d)

# to get the value of d[2]
print("............." , d[2])

# to the get the vale of d[3] which is not present in defaultdictionary, it wil give you 0 instead of key error
print("///////////////// " , d[3])

# however in normal dictinary you will get an error
a = {1: 'habeshaschool', 2: 'java'}
print("-------------" , a[3])


