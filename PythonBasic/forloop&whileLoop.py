import random

student_names_list = ["Jay", "Eshetie", "Jyanti", "Hareg", "hiber", "Amsalu", "tigistu", "Amsalu"]
student_names_tuple = ("Jay", "Eshetie", "Jyanti", "Hareg", "hiber", "Amsalu", "tigistu", "Amsalu")
student_names_set = {"Jay", "Eshetie", "Jyanti", "Hareg", "hiber", "Amsalu", "tigistu", "Amsalu"}
# print using for loop
for name in student_names_set:
    print(name)
    print("*"*10)

size = len(student_names_list)
print(size)
winner_index = random.randint(0, size -1)
for count in range(size):
    if count == winner_index:
        print(student_names_list[count] +  " is the winder ")
    else:
        print(student_names_list[count] + " you are not the winner ")



