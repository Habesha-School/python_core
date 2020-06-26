from collections import Counter

a = [1,1,2,3,2,2,4,5,4,5,4,3,6,2,2]
c = Counter(a)
print("-"*20, c)

#counter has tree more operation that we can perform

# element function, getting all the values inside the counter

print("/"*30, list(c.elements()))

# most common function
print(","*40, c.most_common())

# subtract fuction, subtract 2 one time and subtract 6 one time
sub = {2:1 , 6:1}
c.subtract(sub)
print("."*50, c.most_common())