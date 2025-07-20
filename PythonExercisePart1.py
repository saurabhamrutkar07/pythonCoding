# """  
# 1. Formatted Twinkle Poem

# Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

# """

# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star, \n\tHow I wonder what you are")


# """ 
# 2. Python Version Checker

# Write a Python program to find out what version of Python you are using. 
# """

# import sys 
# print(sys.version)
# print(sys.version_info)


# """ 
# 3. Current DateTime Display

# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14
# """

# import datetime
# print("Current date time ")
# print(datetime.datetime.now())



# """ 
# 4. Circle Area Calculator

# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
# """

# r = 1.1 

# print(f"r = {r}")
# print(f"Area = {3.142 * (r ** 2)}")


# """  
# 5. Reverse Full Name

# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# """

# name = str(input(" Enter your name : "))
# name = name.split()
# print(f"Hello {name[1]} {name[0]}")


# """  
# 6. List and Tuple Generator

# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# """

# values = input("Enter the comma seprated values : ")

# list = values.split(",")
# print(list)

# tuple3 = tuple(list)
# print(tuple3)

# """ 
# 7. File Extension Extractor

# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java
# """

# file_name = input("Enter the name of file : ")

# print(f"Sample file name : {file_name}")
# print(f"The name of the file is : {file_name.split(".")[-1]}")


# """ 
# 8. First and Last Colors

# Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# """

# color_list = ["Red","Green","White" ,"Black"]
# print(f"first color is {color_list[0]}")
# print(f"first color is {color_list[-1]}")



# """ 
# 9. Exam Schedule Formatter

# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014
# """

# exam_st_date = (11,12,2014)
# print(f"The examination will start from : {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")


# """ 
# 10. Number Expansion Calculator

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615
# """

# n = int(input("Enter the positive interger : "))

# # print(n)
# # print(int(str(n) * 2))
# # print(int(str(n) * 3))

# print( n + int(str(n) * 2) + int(str(n) * 3))


# """ 
# 11. Function Documentation Printer

# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.
# """
# # import abs 
# print(abs.__doc__)

# import datetime
# print(datetime.__doc__)


# """ 
# 12. Monthly Calendar Display

# Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.
# """

# month = int(input("Enter the month in mm format: "))
# year = int(input("Enter the year in yyyy format : "))
# if month < 1 or month > 12 :
#     print("Enter the valid months")
# if len(str(year)) > 4 or len(str(year)) < 4 :
#     print("Enter the valid month")

# import calendar
# print(calendar.month(year,month))


# """ 
# 13. Multi-line Here Document

# Write a Python program to print the following 'here document'.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# """

# print("""
# a string that you "don't" have to escape                                                                      
# This                                                                                                          
# is a  ....... multi-line                                                                                      
# heredoc string --------> example 
# """)

# """ 
# 14. Days Between Dates

# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
# """
# from datetime import date
# # date1 = tuple(map(int,input("Enter the first date in yyyy,mm,dd :").split(',')))
# # date2 = tuple(map(int,input("Enter the second date in yyyy,mm,dd format : ").split(',')))
# date1 = tuple(map(int,input("Enter the date one in yyyy,mm,dd format : ").split(',')))
# date2 = tuple(map(int,input("Enter the date two in yyyy,mm,dd format : ").split(',')))
# print(date1, date2)
# difference = date(*date1) - date(*date2)
# print(difference)
# print(difference.days)


# """ 
# 15. Sphere Volume Calculator

# Write a Python program to get the volume of a sphere with radius six.
# """

# radius = int(input("Enter the value of radius : "))
# volume = 4/3 * 3.142 * (radius ** 3)
# print(f"volume of sphere is : {volume}" )


# """ 
# 16. Difference from 17

# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
# """

# num = int(input("Enter the number : "))
# if num > 17 :
#     print(f"the twice of absolute difference between {num} and 17 is {abs(2 * (num - 17))}")
# else :
#     print(f"The difference between {num} and 17 is {17 - num}")


# """ 
# Number Range Tester

# Write a Python program to test whether a number is within 100 of 1000 or 2000.

# """
# import abs 

# n = int(input("Enter the number : "))

# def is_in_range(n):
#     return ((abs(1000 - n )<=100) or (abs(2000 - n) <= 100))


# print(is_in_range(n))


# """ 
# 18. Triple Sum Calculator

# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
# """

# number = (input("Enter comma separated numbers : "))
# num_list = number.split(",")

# if len(num_list) == 3:
#     try:
#         num_list = [int(num.strip()) for num in num_list]
#         if int(num_list[0]) == int(num_list[1]) == int(num_list[2]):
#             print(f"Result is {int(num_list[0]) * 3}")
#         else:
#             result = 0
#             for num in num_list:
#                 result += int(num)

#             print(result) 
#     except ValueError:
#         print("All inputs must be valid integers")

# else:
#     print("Only enter the comma separated 3 valid numbers")


# """
# 19. Prefix "Is" String Modifier

# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
# """

# string = input("Enter the string: ")

# def check_string(input):
#     if len(input) > 2 and input[:2] == "Is":
#         return input 
#     else :
#         new_input = "Is"+ input
#         return new_input
    
# print(check_string(string))


# """ 
# 20. String Copy Generator

# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
# """

# string = input("Enter the string: ")
# n = int(input("Enter the valid non negative number : "))

# def string_copy_generator(text='Hello',num=1):
#     result = ''
#     if text.strip() != '' and num > 0:
#         result = text * num 
#     else:
#         if num < 0 :
#             print("Enter the valid number")
#         if text.split() == "":
#             print("Enter the valid string")
#     if result != '':
#         print(result)

# string_copy_generator(string,n)
# string_copy_generator()


# """ 
# 21. Even or Odd Checker

# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
# """

# n = int(input("Enter the valid integer : "))

# def check_even_or_odd(n=0):
#     result = f"{n} is even number" if n % 2 == 0 else f"{n} is odd number"
#     return result

# print(check_even_or_odd(n))
# print(check_even_or_odd())

# """ 
# 22. Count 4 in List

# Write a Python program to count the number 4 in a given list.
# """

# user_num_list = input("Enter the comma separated numbers : ").split(",")
# # user_num_list = user_num_list.
# print(user_num_list)

# num_list = [int(num.strip()) for num in user_num_list]
# print(num_list)
# def count_of_four(num_list):
#     return num_list.count(4)
# def count_of_four(num_list):
#     count = 0 
#     for num in num_list:
#         if num == 4 :
#             count += 1
#     return count 

# print(f"The count of 4 is {count_of_four(num_list)}")

# """ 
# 23. String Prefix Copies

# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
# """

# string = input("Enter the string : ")
# n = int(input("Enter the number of copies you want : "))

# def get_string_prefix_copies(string='john Doe',no_of_copies=2):
#     result = ''
#     if no_of_copies > 0:
#         if len(string.strip())>2:
#             result += (string[:2] * no_of_copies)
#         elif string.strip() != ''  and len(string.strip()) < 2:
#             result += (string * no_of_copies) 
#     else:
#         result = "Enter valid integer for number of copies which is greater than 0"
    
#     return result

# print(get_string_prefix_copies(string,n))
# print(get_string_prefix_copies())

# """
# 24. Vowel Tester

# Write a Python program to test whether a passed letter is a vowel or not.
# """

# char = input("Enter Character : ")

# def is_vowel(char='a'):
#     # if char in 'aeiou':
#     #     return True
#     # return False 
#     return True if char in "aeiou" else False

# if len(char) != 1:
#     print("Only enter single char ")

# if len(char) == 1:
#    print(is_vowel(char))
# else:
#     print("Only enter single char ")


# """ 
# Value in Group Tester

# Write a Python program that checks whether a specified value is contained within a group of values.

# Test Data:
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False
# """

# test_data1 = [1, 5, 8, 3]
# values = input("Enter comma ',' separated integers : ").split(",")
# values_arr = [int(val) for val in values] 
# value = int(input("Enter the valid intiger :"))

# def is_contained_with_in_group(test_data=[1,2,3,4,5,6,7,8,9,0],val=2):
#     return True if val in test_data else False

# print(is_contained_with_in_group(test_data1,3))
# print(is_contained_with_in_group(test_data1,-1))
# print(is_contained_with_in_group(values_arr,value))
# print(is_contained_with_in_group())

# """
# 26. List Histogram

# Write a Python program to create a histogram from a given list of integers.
# """

# char = input("Enter the any single special char to print : ")
# print("Sample format : 2,3,6,5")
# user_enter_format = input("Enter the format in which you want to print char  :").split(",")
# user_format = [int(char) for char in user_enter_format]

# def print_histogram(char="*",format=[2,3,6,5]):
#     for n in format:
#         print(char * n)     


# if len(char) == 1:
#     print_histogram(char,user_format)
# else:
#     print("Enter valid single character")

# print_histogram()


# """
# 27. List to String Concatenator

# Write a Python program that concatenates all elements in a list into a string and returns it.
# """

# list = ["saurab", "is", "great", "coder" ]
# print(" ".join(list))
# print("Sample input 'this, is , string'")
# user_input = input("Enter the comma ',' separated value :").split(",")
# print("".join(user_input))

# """ 
# 28. Even Numbers Until 237

# Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
# Sample numbers list :

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# """

# number = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
# ]

# for num in number : 
#     if num % 2 == 0:
#            print(num)
#     elif num == 237:
#         print(num)
#         break
        



# """ 
# 29. Unique Colors Finder

# Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}
# """

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# print(color_list_1 - color_list_2)
# print(color_list_1.difference(color_list_2))


# """ 
# 30. Triangle Area Calculator

# Write a Python program that will accept the base and height of a triangle and compute its area.
# """

# base_input = input("Please enter the base of the triangle (a positive whole number): ")
# height_input = input("Please enter the height of the triangle (a positive whole number): ")

# def area_of_triangle(base,height):
#     print (0.5 * base * height)


# if base_input.isdigit() and int(base_input) > 0 and height_input.isdigit() and int(height_input) > 0 :
#     area_of_triangle(int(base_input),int(height_input))
# else:
#     if not(base_input.isdigit() or int(base_input) > 0):
#         print("Enter the valid base input ")
#     elif not(height_input.isdigit() or int(height_input) > 0):
#         print("Please enter the valid height input ")


# """ 
# 31. GCD Calculator

# Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

# """

# x = int(input("Enter the valid integer : "))
# y = int(input("Enter the valid integer : "))

# def get_valid_integers(prompt: str = "Enter two integers separated by comma ',' : ") -> tuple[int,int]:
#     while True:
#         user_input = input(prompt).split(",")
#         if len(user_input) > 2 or len(user_input) < 2:
#             print("Please enter exactly two values")
#         try:
#             x,y = map(int,user_input)
#             return x,y
#         except ValueError:
#             print("Both values must be valid integers ")


# x,y = get_valid_integers()

# print(f"There are the variables set by writing function using advance python {x,y}")


# def get_gcd(x:int,y:int) -> int:
#     x,y = abs(x),abs(y)
#     for i in range((min(x,y)//2),0,-1):
#         if x % i == 0 and y % i == 0 :
#             return i
#     return 1 
            

# print(get_gcd(x,y))

# """ 
# 32. LCM Calculator

# Write a Python program to find the least common multiple (LCM) of two positive integers.
# """

# def get_valid_integers(prompt : str = "Emter two integers separated by cooma ',' : " ) -> tuple[int,int]:
#     while True:
#         user_input = input(prompt).split(",")
#         if len(user_input) > 2 or len(user_input) < 2 :
#             print("Please enter exact 2 values ")
#         try:
#             x,y = map(int, user_input)
#             return x,y
#         except ValueError:
#             print("Both Values must be valid integers ")
        
# x,y = get_valid_integers()

# def get_lcm(x:int,y:int)-> int:
#     z = max(x,y)
#     while True:
#         if z % x == 0 and z % y == 0:
#             lcm =  z 
#             break
#         z += 1
#     return lcm
# print(x,y)
# print(get_lcm(x,y))


# """
# 33. Triple Sum with Equality Rule

# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
# """

# def get_valid_user_input(prompt:str = "Enter the three valid integers separated by comma ',' : ")-> tuple[int,int,int]:
#     while True:
#         user_input = input(prompt).split(",")
#         if len(user_input) > 3 or len(user_input) < 3:
#             print("Please enter exact 3 values ")
#         try:
#             x,y,z = map(int,user_input)
#             return x,y,z
#         except ValueError:
#             print("All Values must be valid integers ")


# x,y,z = get_valid_user_input()

# def triple_sum_equality_rule(a:int=1,b:int=2,c:int=3)-> int:
#     # if a == b or b == c or c == a :
#     #     return 0
#     # else:
#     #     return a + b + c 
    
#     return 0 if a == b or b == c or c == a else a + b + c

# print(triple_sum_equality_rule(x,y,z))
# print(triple_sum_equality_rule())


# """
# 34. Conditional Sum to 20

# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
# """

# def get_valid_user_input(prompt:str = "Enter the two valid integers separated by comma ',' : ")-> tuple[int,int]:
#     while True:
#         user_input = input(prompt).split(",")
#         if len(user_input) > 2 or len(user_input) < 2: 
#             print('Please enter exact two values ')
#         try :
#             x,y = map(int,user_input)
#             return x,y
#         except ValueError:
#             print("All values must be valid intergers ")

# x,y = get_valid_user_input()

# def conditional_sum_to_20(x:int,y:int)-> int:
#     if x + y >= 15 and x + y <= 20:
#         return 20 
#     else:
#         return x + y  

# print(f" The conditional sum of {x} and {y} is {conditional_sum_to_20(x,y)}")

# """
# 35. Equality or 5 Rule Checker

# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
# """

# def get_valid_user_input(prompt="Enter the two valid integers separated by comma ',' ")-> tuple[int,int]:
#     while True :
#         user_input = input(prompt).split(",")
#         if len(user_input) > 2 or len(user_input) < 2 :
#             print('Please enter exact 2 values ')
#         try :
#             x,y = map(int,user_input)
#             return abs(x),abs(y)  
#         except ValueError:
#             print('All values must be valid integers')
# x,y = get_valid_user_input()

# def equality_or_five_rule_checker(a:int,b:int)-> int:
#     return True if a == b or (a + b == 5 ) or (a - b == 5 ) else False


# print(equality_or_five_rule_checker(x,y))


