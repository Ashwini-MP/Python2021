# 1. Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”
string = input('Enter the string: ')
print(string[::-1])

# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12
string = input('Enter the string: ')
u = 0
l = 0
for i in string:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1
print(f'No.of Upper characters: {u}, No.of Lower case characters: {l}')

# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
def remove_duplicates(l):
    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)
    return new_list


l = list(input('Enter the elements of list separated by comma:').split(','))
print(remove_duplicates(l))

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.
words = input('Enter sequence of words separated by hyphen: ').split('-')
words.sort()
print('-'.join(words))

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break

for l in lines:
    print(l)

# 6. Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console.
def addition(a, b):
    print(int(a)+int(b))


num1 = input('enter the first number: ')
num2 = input('enter the second number: ')
addition(num1, num2)

# 7. Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.
def longest_string(s1,s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s1) == len(s2):
        print(s1)
        print(s2)
    else:
        print(s2)


string1 = input('Enter the first string: ')
string2 = input('Enter the second string: ')
longest_string(string1, string2)

# 8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).
def square_of_numbers():
    x = []
    for i in range(1,21):
        x.append(i**2)
    print(tuple(x))

square_of_numbers()

# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
def showNumbers(limit):
    for i in range(0, limit+1):
        if i % 2 == 0:
            print(f'{i}: EVEN ')
        else:
            print(f'{i}: ODD ')


showNumbers(3)

# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)
print(list(filter(lambda a: a % 2 == 0, range(1, 21))))

# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define anonymous functions.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, my_list)))
print(new_list)

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions
def divide():
    return 5/0


try:
    divide()
except Exception as ex:
    print("The error is ", ex)

# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
my_list = [1, 2, 3, 4, 5, 6, 7]
print(reduce(lambda x, y: str(x) + str(y), my_list))

# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.
values = input("Enter the list of numbers separated by comma: ").split(',')
my_list = list(values)
print(list(filter(lambda a: eval(a) % 3 != 0 and eval(a) % 7 == 0, my_list)))

# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.

def multiply(l):
    return l*l


values = eval(input("Enter the list of numbers separated by comma: "))
my_list = list(values)
result = map(multiply, my_list)
print(list(result))

# 16. What is the output of the following codes:

(i) def foo():
try:
return 1
finally:
return 2
k = foo()
print(k)
Answer: 2

(ii) def a():
try:
f(x, 4)
finally:
print('after f')
print('after f?')
a()
Answer: after f
               after f?
Name Error: name ‘f’ is not defined





















