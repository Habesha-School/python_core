
""" dictioniary stores key, value paris
key can ben any thing ( string, int, float)
but should be unique ==> set"""

student_info = {111: ("Jay", 25, 301999999),
                222: "Eshetie",
                333: "Jyanti",
                444: "Hareg",
                555: "hiber",
                666: "Amsalu",
                777: "tigistu",
                888: "Amsalu",
                888: "Ali"
                }

# printing all in one
print(student_info)

# printing values by key
print(student_info[555])

# repalce the value of 888
student_info[888] = "Beza"

# print all
print(student_info)
print(student_info[888])

print(student_info[111][1])

# features of dictionary
which_student_popped = student_info.pop(777)

print(which_student_popped)
print(student_info)
student_copy = student_info.copy()
print("*"*20 + "printing after copy ")
print(student_copy)

print(student_info.keys())
print(student_info.values())








