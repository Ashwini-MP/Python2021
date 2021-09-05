# # # 1. Create a list of given structure and get the Access list as provided below:
# x = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# access_list = x[5][0:4]
# print(f'access_list:{access_list}')
# access_list = x[6:8]
# print(f'access_list:{access_list}')
# access_list = x[::2]
# print(f'access_list:{access_list}')
# access_list = x[::-1]
# print(f'access_list:{access_list}')
# access_list = x[5][5][0]
# print(f'access_list:{access_list}')
# x.clear()
# print(f'access_list:{x}')

# 2. Create a list of thousand numbers using range and xrange and see the difference between each
# other.
# # l = list(range(1,1001))
# # print(l)
#
# xl = list(xrange(1,1001))
# print(xl)


# How Tuple is beneficial as compared to the list?
# Tuples are faster than lists.
# It makes our code safer if we “write-protect” data that does not need to be changed.

# 4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
# the number which is divisible by 3 and is a multiple of 2.
# for i in range(1,101):
#     if i % 3 == 0 and i % 2 == 0:
#         print(i)

# 5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
# string with their index.
# string = input('Enter the string: ')
# rev = string[::-1]
# # print(rev)
# vowels = 'aeiouAEIOU'
# for i in range(len(rev)):
#     if rev[i] in vowels:
#         print(f 'index: {i}, alphabet: {rev[i]}')



# 6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
# string which is having an even length.
# string = "hello my name is abcde".split(' ')
# print(string)
# for i in string:
#     if len(i)%2 == 0:
#         print(i)

# 7. Write a program in python to print the pair of numbers whose sum is equal to the result
# number that is let's say 8.

# result = 8
# x = [1,2,3,4,5,6,7,8,9,-1]
# for i in range(len(x)):
#     for j in range(i+1, len(x)):
#         if x[i]+x[j] == result:
#             print(x[i],x[j])



# 8. Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list
# Ask user to enter a number in the range of 1,50 and make sure if the entered number is
# even, append it to the even_list and if the entered number is odd append it to the odd_list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you enter all the 5 elements, calculate the sum of the list and return the
# maximum of the list.


# def addition(l):
#     result = 0
#     for x in l:
#         result += x
#     return result
#
#
# even_list = []
# odd_list = []
# i = 0
# while i < 10:
#     number = eval(input('Enter a number in the range of 1,50: '))
#     if number % 2 == 0 and len(even_list) < 5:
#         even_list.append(number)
#         # addition(even_list)
#         # for x in even_list:
#         #     result_even += x
#         # print(even_list, result_even)
#     elif number % 2 != 0 and len(odd_list) < 5:
#         odd_list.append(number)
#         # addition(odd_list)
#         # for x in odd_list:
#         #     result_odd += x
#         # print(odd_list, result_odd)
#     i += 1
# if addition(even_list) > addition(odd_list):
#     print(addition(even_list))
# else:
#     print(addition(odd_list))

# 9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
# string = input('Enter a string: ')
# newlist = []
# for char in string:
#     if char.isalpha() and char not in newlist:
#         newlist.append(char)
# for item in newlist:
#         print(f'The occurance of the character {item} is: {string.count(item)}')

# 10. Generate and print another tuple whose values are even numbers in the given tuple
# my_tuple = (1,2,3,4,5,6,7,8,9,10)
# my_list = []
# for i in my_tuple:
#     if i % 2 == 0:
#         my_list.append(i)
# new_tuple = tuple(my_list)
# print(new_tuple)









