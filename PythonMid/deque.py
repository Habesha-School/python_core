from collections import deque

a = ['e','d','u','r','e', 'k', 'a']
d = deque(a)
print(d)

# append a value
d.append('z')
print(d)

# if you want to append a value to the beginning
d.appendleft('x')
print(d)

# if you want to remove a value

d.pop()
print(d)

# remove a value from the begining
d.popleft()
print(d)
