# 1. Create three variables in a single line and assign values to them in such a manner that each one of them belongs to a different data type.
a, b, c = 1, 2.01, 'string'

# 2. Create a variable of type complex and swap it with another variable of type integer
a = 1+2j
b = 12
a, b = b, a
print(a)
print(b)

# 3. Swap two numbers using a third variable and do the same task without using any third variable.
a = 5
b = 7
temp = a
a = b
b = temp
print(a)
print(b)

a = 5
b = 12
a, b = b, a
print(a)
print(b)

# 4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.
Python 3.x Version:
name = input('Please enter your name: ')
print(name)

Python 2.x Version
name = raw_input('Please enter your name: ')
print(name)

# 5. Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output.
first_number = eval(input('Enter any number between 1-10: '))
second_number = eval(input('Enter any number between 1-10: '))
z = first_number + second_number
result = 30 + z
print(result)

# 6. Write a program to check the data type of the entered values.
x = eval(input('Enter the input value: '))
print('The data type of the input value is:', type(x))

# 7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
UPPERCASE.
# Upper camel case/Pascal case
FirstNumber = 10
# Lower camel case
inputNumber = 20
# snake case
second_number = 30
# Upper case
NAME = 'Ashwini'

# 8.If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value? If Yes then Why?
Answer: Yes, the value of the variable ‘a’ will be changed because python is a dynamically typed programming language. Variables do not need to be declared with any particular type and can even change type after they have been set.






