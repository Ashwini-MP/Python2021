# 1. # Create a list of 10 elements of four different data types like int, string, complex and float.
my_list = [10, 20, 10.1, 20.1, 'text', 'num', 1+2j, 5j, 50, 45]
print(len(my_list))

# 2. Create a list of size 5 and execute the slicing structure
#te

my_list = [10, 20, 10.1, 20.1, 'text']
print(my_list[:])
print(my_list[0:])
print(my_list[:-1])
print(my_list[::-1])

# 3. Write a program to get the sum and multiply of all the items in a given list.
my_list = [-1, 2, 3, 4]
sum = 0
for i in my_list:
    sum += i
print(sum)

my_list = [-1, 2, 3]
product = 1
for i in my_list:
    product *= i
print(product)

# 4. Find the largest and smallest number from a given list.
my_list = [50, 8, 20, 10]
largest_number = my_list[0]
for i in my_list:
    if i > largest_number:
        largest_number = i
print(largest_number)

my_list = [50, 8, 20, 10]
smallest_number = my_list[0]
for i in my_list:
    if i < smallest_number:
        smallest_number = i
print(smallest_number)

# 5. Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list.
l1 = [50, 8, 53, 23, 20, 10]
l2 = []
for i in l1:
    if i % 2 != 0:
        l2.append(i)
print(l2)

# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and30 (both included).
l = list()
for i in range(1, 31):
    l.append(i**2)
print(l)
print(l[:5])
print(l[-5:])

# 7. Write a program to replace the last element in a list with another list.
l1 = [10, 20, 30, 40, 50]
l2 = [1, 2, 3]
l1[-1] = l2
print(l1)

# 8. Create a new dictionary by concatenating the following two dictionaries:
a = {1:10, 2:20}
b = {3:30, 4:40}
c = {**a, **b}
print(c)

# 9. Create a dictionary that contain numbers in the form(x: x*x) where x takes all the values between 1
# and n(both 1 and n included).
n = int(input('Enter the value of n:'))
my_dict = {}
for i in range(1, n+1):
    my_dict[i] = i*i
print(my_dict)

# 10. Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.
num = input('Enter the elements separated by comma: ').split(',')
l = list(num)
t = tuple(l)
print(l)
print(t)





