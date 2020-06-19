student_names_list = ["Jay", "Eshetie", "Jyanti", "Hareg", "hiber", "Amsalu", "tigistu", "Amsalu"]
student_names_tuple = ("Jay", "Eshetie", "Jyanti", "Hareg", "hiber", "Amsalu", "tigistu", "Amsalu")
student_names_set = {"Jay", "Eshetie", "Jyanti", "Hareg", "hiber", "Amsalu", "tigistu", "Amsalu"}
print("*"*10 + "list" + str(student_names_list))
print("*"*10 + "tuple" + str(student_names_tuple))
print("*"*10 + "set" + str(student_names_set))

# can we addend values
student_names_list.append("Mukmil")
student_names_set.add("Mukmil")
print("\n")
print("*"*10 + "list" + str(student_names_list))
print("*"*10 + "tuple" + str(student_names_tuple))
print("*"*10 + "set" + str(student_names_set))