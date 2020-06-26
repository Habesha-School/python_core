names = ['ehsete' , ' tefaye']  # prepopulated list
scores = []  # empty list
scores.append(100) # add new item to the end
scores.append(99) # add new item to the end
print(names)
print(scores)

#
print(scores[0])

# Arrays are collection of items

from array import array

scores = array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

# the difference between Array and List is
# Array has to be numeric days types and alwys must be the sme days types
# List cam store any data type

# common operations

names = ['tesfaye' , 'eshete']
print(len(names)) # get the nubmer of items
names.insert(0, 'Solomon') # insert before index
print(names)
names.sort() # sort
print(names)

# retrieving ranges

names = ['eshete', 'tesfaye', 'solomon' , 'habetu']
print("all names", names)
# start and end end index
presenters = names [1:3]
print("name of presenters", presenters)

# give me all the index but not including last index

presenters = names [ :3]
print("name of presenters", presenters)