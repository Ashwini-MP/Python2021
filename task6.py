# 1.Write a program in Python to find out the character in a string which is uppercase using list
# comprehension.

string = input('Enter the string: ')
l = [i for i in string if i.isupper()]
print(l)

#2. Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.

students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
d = {}
for key in students:
    for value in subjects:
        d[key] = value
        subjects.remove(value)
        break
print(d)

# using dictionary comprehension
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
d = {students[i]: subjects[i] for i in range(len(students))}
print(d)

# using zip function
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
d = dict(zip(students, subjects))
print(d)

# 4. Write a program in Python using generators to reverse the string.
def string_rev(s):
    length = len(s)
    for i in range(length-1, -1, -1):
        yield s[i]


s = input('Enter the string: ')
for char in string_rev(s):
    print(char)

#5. Write an example on decorators.
# Program to avoid negative result

def difference(a,b):
    r = a-b
    return r

def sd(func):
    def inner(a,b):
        if b > a:
            a, b = b, a
        return func(a, b)
    return inner


num1 = eval(input('Enter the first number: '))
num2 = eval(input('Enter the second number: '))
dr = sd(difference)
print(dr(num1, num2))



