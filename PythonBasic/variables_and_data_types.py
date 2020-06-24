"""  This program is to learn about pyton
variables
data types ( string, int float, boolean)
and string connection using a + and format method
"""

# you don't need to add ; to the end of python statements

first_name = "solomon"  # string
last_name = "Habut"
age = 35  # int
hight = 1.6  # float or double
weight = 85  # int
gender = 'M'  # char
is_student = False  # boolean = > 0
is_professor = True  # boolean > 1
full_name = "My full name is " + first_name + " " + last_name  # concatinating using a + plus singe
print(full_name)

full_name = "my full name is {} {}".format(first_name, last_name)
print(full_name)
print(age)
print(weight)

print(is_student)

# split string
name_split_by_space = full_name.split(" ")  # ["my",  "full",  "name",  "is", "solomon", "habut"]
print("*"*10)
print(name_split_by_space[0])
print(name_split_by_space[5])


