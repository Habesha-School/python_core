
"""" tuple is a non immutable ( not modifiable) collection """

student_names = ("Jay", "Eshetie", "Jyanti", "Hareg",
                 "hiber", "Amsalu", "tigistu", "Amsalu")
print(student_names[5])
print(student_names[5:])
number_of_students = len(student_names)
print("total number of studetns {}".format(number_of_students))
print(student_names.count("Amsalu"))
print(student_names)
