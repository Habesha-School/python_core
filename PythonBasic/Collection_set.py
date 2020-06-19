""" only unique record will be stored in a set
it is not indexed, it is unordered
pop, add"""
student_names = {"Jay", "Eshetie", "Jyanti", "Hareg", "hiber", "Amsalu", "tigistu", "Amsalu"}
print(student_names)
print("poping last record " + student_names.pop())
print(student_names)

student_names.add("Ämsalu")
student_names.add("Bez")
print(student_names)
