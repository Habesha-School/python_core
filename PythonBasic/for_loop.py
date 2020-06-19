""""
 this program is to identify even and odd numbers
sum even numbers and odd numbers separately
and finally print the result on the console
"""

# variables to store sum of even and odd numbers
max_number = input("Inter the max number:")
max_number = int(max_number)
sum_of_odd_numbers = 0
sum_of_even_number = 0
sum_of_all_numbers = 0

# for loop to iterate till the given number
for i in range(max_number + 1):

    # identify even number
    if i % 2 == 0:
        print(str(i) + "is even")
        sum_of_even_number = sum_of_even_number + i
    else:
        # identify odd number
        print(str(i) + "is odd number")
        sum_of_odd_numbers = sum_of_odd_numbers + i

    # adding all numbers
    sum_of_all_numbers = sum_of_all_numbers + i

# print sum of odd and even numbers up to the given number
print("*"*30)
print("Sum of even numbers up to {} is {}".format(max_number, sum_of_even_number))
print("Sum of odd numbers up to {} is {}".format(max_number, sum_of_odd_numbers))
print("sum of numbers up to {} is {}".format(max_number, sum_of_all_numbers))


