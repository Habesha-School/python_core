student_names = ["Jay", "Eshetie", "Jyanti", "Hareg", "hiber", "Amsalu", "tigistu"]
print(student_names)
# if you get data from the databse
# if you get data from studnets
student_names.append("Amsalu")
student_names.append("Amsalu")

print(student_names[-1])
count_of_amsalu= student_names.count("Amsalu")
print(count_of_amsalu)

# print after adding amsalu 3 times
print(student_names)

which_value_is_popped = student_names.pop()
print("pop the last record is " + which_value_is_popped)
# clear the list
# student_names.clear()
print(student_names)
student_names.sort()
print(student_names)
print(student_names[3:6])
print(student_names[-3:])