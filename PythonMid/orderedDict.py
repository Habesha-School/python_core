from collections import OrderedDict


d = OrderedDict()
d[1] = 'e'
d[2] = 'd'
d[3] = 'u'
d[4] = 'r'
d[5] = 'e'
d[6] = 'k'
d[7] = 'a'

print(d)

print(d.keys())

# change the value
d[1] = 'x'
print(d)


