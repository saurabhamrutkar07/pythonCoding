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

# """
# 36. Add Integers Validator

# Write a Python program to add two objects if both objects are integers.
# """


# def add_numbers(a,b):
#     if not (isinstance(a,int) and isinstance(b,int)):
#         return "Inputs must be integers"
#     return a + b 


# print(add_numbers(10,20))
# print(add_numbers(10,20.23))
# print(add_numbers('5',6))
# print(add_numbers('5','6'))


# """
# Personal Info Formatter

# Write a Python program that displays your name, age, and address on three different lines.
# """

# def personal_info():
#     name, age = 'Saurabh Amrutkar',20
#     address = 'Pune, Maharashtra, India'

#     return f"\nName : {name} \nAge : {age} \nAddress : {address}"


# print(personal_info())


# """ 
# Expression Solver

# Write a Python program to solve (x + y) * (x + y).

# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49
# """

# def get_valid_user_input(prompt: str = "Enter the two valid integers separated by comma ',' : ")-> tuple[int,int]:
#     while True:
#         user_input = input(prompt).split(",")
#         if len(user_input) > 2 or len(user_input) < 2:
#             print("Please enter exact 2 values")
#         try :
#             x,y  = map(int,user_input)
#             return abs(x),abs(y)
#         except ValueError:
#             print("All values must be valid integers")
        
# x,y = get_valid_user_input()

# def expression_solver(a:int=4,b:int=3)-> int:
#     return((a + b) ** 2)


# print(expression_solver())
# print(expression_solver(x,y))


# """
# Future Value Calculator

# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.

# The formula for future value with compound interest is FV = P(1 + r/n)^nt.
# FV = the future value;
# P = the principal;
# r = the annual interest rate expressed as a decimal;
# n = the number of times interest is paid each year; 0.01
# t = time in years.
# """

# def get_valid_user_input(prompt:str="Enter principal, annual interest rate (decimal) and time in years separated by commas: ")-> tuple[float,float,float]:
#     while True:
#         user_input = input(prompt).split(',')
#         if len(user_input )> 3 or len(user_input) < 3:
#             print("Please enter exact 3 values")
#         try:
#             x,y,z = map(float,user_input)
#             return x,y,z
#         except ValueError:
#             print("All values must be valif floats ")
        
# x,y,z = get_valid_user_input()

# def future_value_calculator(principle:float=10000.00,rate:float=3.5,time:float=7.0) -> float:
#     n = 0.01
#     return round(principle * ((1 + 0.01 * rate)) ** ( time),2)


# print(f"The future value of load is Rs.{future_value_calculator(x,y,z)}")
# print(f"The future value of load is Rs.{future_value_calculator()}")


# """
# 40. Distance Between Points

# Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
# """

# import math 

# def get_point_input(prompt:str="Enter the comma ',' point as x,y: ")->list[int]:
#     while True:
#         user_input = input(prompt).split(",")
#         if len(user_input) > 2 or len(user_input) < 2:
#             print("Please enter exactly 2 values separated by comma ")
#         try:
#             points = [int(value.strip()) for value in user_input]
#             return points
#         except ValueError:
#             print("Both values must be valid integers ")
        
# p1 = get_point_input()
# p2 = get_point_input()

# def distence_between_points(p1=[4,0],p2=[6,6]):
#     return math.sqrt((p1[0] - p2[0]) ** 2 ) + ((p1[1] - p2[1]) ** 2)

# print(f"distance between points is {distence_between_points(p1,p2)}")
# print(f"distance between points is {distence_between_points()}")
        
    

# """
# 41. File Existence Checker

# Write a Python program to check whether a file exists.
# """

# import os.path 

# print(os.path.isfile('PythonExercisePart1.py'))
# print(os.path.isfile("04PythonDataTypes.py"))
# print(os.path.isfile("04.PythonDataType.py"))


# """
# 42. Shell Mode Detector

# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
# """

# import struct
# print(struct.calcsize("P") * 8)

# import platform

# print(platform.architecture())
# print(platform.architecture()[0])


# """
# 43. OS and Platform Info

# Write a Python program to get OS name, platform and release information.
# """

# import platform 
# import os 

# print(os.name)
# print(platform.system())
# print(platform.release())

# """
# 44. Python Site Packages Locator

# Write a Python program to locate Python site packages.
# """

# import site
# print(site.getsitepackages())


# """
# 45. External Command Runner
# This is code is outdate not working 

# Write a Python program that calls an external command.
# """
# from subprocess import call 

# call(["ls", "-l"])

# """
# 46. File Path and Name Finder

# Write a Python program to retrieve the path and name of the file currently being executed.
# """

# import os 
# print(f"Path of the file is : {os.path.realpath(__file__)}")

# """
# 47. CPU Count Finder

# Write a Python program to find out the number of CPUs used.
# """

# import multiprocessing

# print(multiprocessing.cpu_count())


# """
# 48. String to Numeric Parser

# Write a Python program to parse a string to float or integer.
# """

# def get_valid_user_input(prompt:str="Enter the valid number : ")->(str):
#     return input(prompt)

# a = get_valid_user_input()
# b = get_valid_user_input()

# def string_parser(num="34"):
#     return float(num) if "." in num else int(num) 

# print(string_parser(a))
# print(string_parser(b))
# print(string_parser())


# """
# 49. Directory Files Lister

# Write a Python program to list all files in a directory.
# """

# from os import listdir
# from os.path import isfile,join 

# files_list = [f for f in listdir('C:/Users/HP/Desktop/PythonPractice') if isfile(join('C:/Users/HP/Desktop/PythonPractice', f))]
# print(files_list)

# """
# 50. Print Without Newline

# Write a Python program to print without a newline or space.
# """

# for i in range(1,11):
#     print("*",end="")
# print("\n")

# for i in range(1,11):
#     print("*")


# """
# 51. Program Profiler

# Write a Python program to determine the profiling of Python programs.
# Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.
# """
# import cProfile 
# def sum():
#     print(1 + 2)

# cProfile.run('sum')


# """
# 57. Method Execution Time

# Write a Python program to get the execution time of a Python method.
# """
# import time
# n = int(input("Enter the valid integer : "))

# def get_method_execution_time(n):
#     start_time = time.time()
#     print(start_time)
#     s = 0
#     for i in range(1,n+1):
#         s += i 

#     end_time = time.time()
#     print(end_time)
#     execution_time = end_time - start_time
#     return s , execution_time

# print(get_method_execution_time(n))


# """
# 58. Sum of First n Positives

# Write a Python program to sum the first n positive integers.
# """

# n = int(input("Enter the positive integer : "))
# def get_sum_of_first_n_numbers(n=5):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i 

#     return sum

# print(get_sum_of_first_n_numbers(n))
# print(get_sum_of_first_n_numbers())

# """
# 59. Height to Centimeters

# Write a Python program to convert height (in feet and inches) to centimeters.
# """

# print("Enter the height :")
# ft = int(input("Feet : "))
# inch = int(input("Inch : "))

# def get_height_in_cm(inch=10,ft=5):
#     totalinch = inch + ( ft * 12) 
#     height_in_cm = totalinch * 2.54
#     return f"The height for {ft} feet and {inch} inches is {height_in_cm} cm."


# print(get_height_in_cm(inch,ft))

# """
# 60. Triangle Hypotenuse Calculator

# Write a Python program to calculate the hypotenuse of a right angled triangle.
# """
# import math
# def get_two_smaller_sides_of_traingle(prompt:str="Enter two smaller sides of traingle separated with comma ',' : ")->tuple[float,float]:
#     while True:
#         user_input = input(prompt).split(",")
#         if len(user_input)> 2 or len(user_input) < 2:
#             print("Please enter exactly 2 values separated by comma ")
#         try:
#             x,y = map(float, user_input)
#             return x,y
#         except ValueError:
#             print("Both values must be valid numbers ")

# x,y = get_two_smaller_sides_of_traingle()

# def calculate_triangle_hypoteneous(x=3.0,y=4.0):
#     result = round(math.sqrt (x ** 2 + y ** 2),2)
#     return f"The hypoteneous of triangle is {result}"

# print(calculate_triangle_hypoteneous(x,y))
# print(calculate_triangle_hypoteneous())


# """
# 62. Time to Seconds Converter

# Write a Python program to convert all units of time into seconds.
# """

# days = int(input("Enter the days : ")) * 3600 * 24

# hours = int(input("Enter the hours : ")) * 3600

# minutes = int(input("Enter the minutes : ")) * 60

# seconds = int(input("Enter the seconds : "))

# time = days + hours + minutes + seconds

# print(f"The  amounts of seconds {time}")


# """
# 65. Seconds to DHMS Converter

# Write a Python program that converts seconds into days, hours, minutes, and seconds.
# """

# seconds = int(input("Enter the seconds : "))

# def seconds_to_DHMS_converter(seconds:int=7200)->str:
#     origina_seconds = seconds
#     days = seconds // (3600 * 24)
#     seconds %= (3600 * 24)
#     hours = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60 
#     seconds %= 60 
#     return f"{origina_seconds} seconds = {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"   

# print(seconds_to_DHMS_converter(seconds))
# print(seconds_to_DHMS_converter(4578546))
# print(seconds_to_DHMS_converter()) 


# """
# 66. BMI Calculator

# Write a Python program to calculate the body mass index.
# """

# def get_valid_float(prompt:str)->float:
#     while True:
#         try:
#             user_input = float(input(prompt))
#             if user_input <0:
#                 print("Please enter positive number")
#             else:
#                 return user_input
#         except ValueError:
#             print("Invalid Input. Please Enter numeric value")

# def get_valid_gender(prompt:str)->str:
#     while True:
#         user_input = input(prompt)
#         try:
#             if user_input.lower() in ['m','f']:
#                 return user_input
#             else:
#                 print("Invalid gender ")

#         except ValueError:
#             print("Please enter vlaue among M,F")

# height = get_valid_float("Enter the helight : ")
# weight = get_valid_float("Enter the weight : ")
# #gender = get_valid_gender("Enter your gender : ")

# def calculate_bmi(height:float=165,weight:float=65)->float:
#     return round(weight / (height ** 2),2)

# def get_bmi_category(bmi:float=24)->str:
#     if bmi < 18.5:
#         return f"Your BMI is {bmi} and you come under UNDERWEIGHT Category"
#     elif 18.5 <= bmi <= 24.9:
#         return f"Your BMI is {bmi} and you come under NORMAL Category"
#     elif 25 <= bmi <= 29.9:
#         return f"Your BMI is {bmi} and you come under OVERWEIGHT Category"
#     elif 30 <= bmi <= 34.9:
#         return f"Your BMI is {bmi} and you come under OBES Category"
#     elif bmi >= 35:
#         return f"Your BMI is {bmi} and you come under EXTREMLYOBES Category"
    

# bmi = calculate_bmi(height,weight)
# category = get_bmi_category(bmi)

# print(f"Your BMI is {bmi} {category}")

# """
# Sum of Digits

# Write a Python program to calculate sum of digits of a number.
# """

# def get_valid_input(promt:str="Enter valid integer : ")-> str:
#     while True :
#         user_input = input(promt)
#         try:
#             if user_input.isdigit():
#                 return user_input
#             else:
#                 print("The input is invalid please enter valid inputs :")

#         except ValueError:
#             print("Enter the valid integer ")


# number = get_valid_input()

# def get_sum_of_digits(number:str='12345')->int:
#     sum = 0 
#     for num in number:
#         sum += int(num)

#     return f"The sum of digits of number {number} is {sum}"

# print(get_sum_of_digits(number)) 
# print(get_sum_of_digits())

# """ different way """

# def get_valid_number(promt:str="Enter valid integer : ")-> str:
#     while True :
#         user_input = input(promt)
#         try:
#             if user_input.isdigit():
#                 return int(user_input)
#             else:
#                 print("The input is invalid please enter valid inputs :")

#         except ValueError:
#             print("Enter the valid integer ")


# number = get_valid_number()

# def get_sum_of_digits_from_int(number:int=12345)->int:
#     original_number = number
#     sum = 0
#     while number >0:
#         sum += number % 10 
#         number = number // 10 
#     return f"The sum of digits of number {original_number} is {sum}"

# print(get_sum_of_digits_from_int(number))
# print(get_sum_of_digits_from_int())


# """
# 67. Pressure Unit Converter

# Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
# """

# kpa = float(input("Input pressure in kilopascals: "))

# # Convert kilopascals to pounds per square inch (psi) using the conversion factor.
# psi = kpa / 6.89475729

# # Convert kilopascals to millimeters of mercury (mmHg) using the conversion factor.
# mmhg = kpa * 760 / 101.325

# # Convert kilopascals to atmospheres (atm) using the conversion factor.
# atm = kpa / 101.325

# # Print the pressure in pounds per square inch (psi) with 2 decimal places.
# print("The pressure in pounds per square inch: %.2f psi"  % (psi))

# # Print the pressure in millimeters of mercury (mmHg) with 2 decimal places.
# print("The pressure in millimeters of mercury: %.2f mmHg" % (mmhg))

# # Print the atmosphere pressure (atm) with 2 decimal places.
# print("Atmosphere pressure: %.2f atm." % (atm))


# """
# 69. Sort Three Numbers

# Write a Python program to sort three integers without using conditional statements and loops.
# """
# def get_valid_user_input(prompt:str="Enter the valid integer: ")->int:
#     while True:
#         user_input = input(prompt).strip()
#         if user_input.isdigit():
#             return int(user_input)
#         else:
#             print("Invalid Integer : ")

# a = get_valid_user_input()
# b = get_valid_user_input()
# c = get_valid_user_input()

# def sort_three_numbers(a:int=2,b:int=4,c:int=5)->tuple[int,int,int]:
#     if a > b :
#         a,b = b,a 
    
#     if b > c : 
#         b,c = c,b 

#     if a > b :
#         a,b = b,a 
    
#     return a,b,c 

# print(sort_three_numbers(a,b,c))
# print(sort_three_numbers())

# """ Another approach """

# def sort_three_numbers_method_2(a:int=2,b:int=4,c:int=5)->tuple[int,int,int]:
#     if a <= b and a <= c :
#         if b <= c:
#             return a,b,c 
#         else :
#             return a,c,b

#     elif b <= a and b <= c:
#         if a <= c :
#             return b,a,c 
#         else:
#             return b,c,a 
    
#     else:
#         if a <= b :
#             return c,a,b
#         else:
#             return c,b,a
# print(sort_three_numbers_method_2(a,b,c))
# print(sort_three_numbers_method_2())


# """
# 70. Sort Files by Date

# Write a Python program to sort files by date.
# """

# import os 
# import math

# # for i in (dir(os)):
# #     print(f"The op of this {i} is : ")
# #     print(os.{i}())

# print(os.listdir("."))

# # print(os.path.isfile("Patterns.py"))

# files = []
# for file in os.listdir("."):
#     if os.path.isfile(file):
#         files.append(file)

# print("Files without modified time : ")        
# print(files)
# files.sort(key=lambda x: os.path.getmtime(x))

# print("Files with modified time olders first : ")

# print(files)

# import os 
# import time

# print(os.listdir("../my Projects"))

# #files = [f for f in os.listdir("../my Projects") if os.path.isfile(os.path.join(os.listdir(f"../my Projects/{f}")))]

# files = [f for f in os.listdir("../my Projects") if os.path.isdir(os.path.join("../my Projects", f))]


# files.sort(key= lambda x : os.path.getctime(os.path.join("../my Projects",x)) )

# print(files)

# for file in files:
#     print(file)
#     print(f"{os.path.join("../my Projects",file)}  {time.ctime(os.path.getctime(os.path.join("../my Projects",file)))}")


# """
# 72. Math Module Details

# Write a Python program to get the details of the math module.
# """

# import math 

# print(dir(math))


# """
# Line Midpoint Calculator

# Write a Python program to calculate the midpoints of a line.
# """

# def get_valid_user_input(prompt= "Enter the comma separated ',' co-ordinated of line : ")->tuple[int,int]:
#     while True:
#         user_input = input(prompt).split(",")
#         if len(user_input) != 2:
#             prin("Enter exact 2 numbers :")
#         try:
#             a,b = map(int,user_input)
#             return a,b 
#         except ValueError :
#             print('Please enter valid input ')



# x1,y1 = get_valid_user_input()
# x2,y2 = get_valid_user_input()

# print(x1,x2)
# print(y1,y2)

# def midline_calculator(x1,y1,x2,y2):
#    return ((x1 + x2)/2),((y1+y2)/2)


# print(f"the mid point of line with co-ordiantes {x1,y1} and {x2,y2} is {midline_calculator(x1,y1,x2,y2)}")



# """
# 74. Word Hasher

# Write a Python program to hash a word.
# """

# word = input("Enter a word : ").strip()

# word = word.upper()


# soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]


# coded_word = word[0]

# for i in word[1:]:
#     order =  ord(i) - 65
#     coded_word += str(soundex[order])

# print(coded_word)


# """
# 75. Copyright Information

# Write a Python program to get the copyright information and write Copyright information in Python code.
# """

# print(copyright)

# import sys

# print(sys.copyright)

# 76 is not able ot understand 

# """
# Test whether the system is a big-endian platform or little-endian platform
# """


# import sys 

# print()

# print(dir(sys))

# print(sys.byteorder)

# if sys.byteorder == 'little':
#     print("Little Eding platform")
# else:
#     print("Big Ending Platform")

# """
# 78. List Built-in Modules

# Write a Python program to find the available built-in modules.
# """

# import sys

# print(dir(sys))
# print()
# print(sys.builtin_module_names)

# for module in sys.builtin_module_names:
#     print(module)

# """
# 79. Object Size Finder

# Write a Python program to get the size of an object in bytes.
# """

# import sys 

# print(dir(sys))

# str1 = 'one'
# str2 = 'four'
# str3 = 'two'

# x = 0
# y = 27
# w = 112
# z = 112.26


# print(f"the size of {str1} is {sys.getsizeof(str1)} bytes")
# print(f"the size of {str2} is {sys.getsizeof(str2)} bytes")
# print(f"the size of {str3} is {sys.getsizeof(str3)} bytes")
# print(f"the size of {x} is {sys.getsizeof(x)} bytes")
# print(f"the size of {y} is {sys.getsizeof(y)} bytes")
# print(f"the size of {z} is {sys.getsizeof(z)} bytes")
# print(f"the size of {w} is {sys.getsizeof(w)} bytes")


# """
# 80. Current Recursion Limit

# Write a Python program to get the current value of the recursion limit.
# """

# import sys
# print(dir(sys))

# print(f"ths current size of recursion {sys.getrecursionlimit()}")


# """
# 150. Odd Product Pair Checker

# Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values.
# """

# def get_user_define_list()->list[int]:
#     """
#     Prompts the user to enter the number of elements, then collects that many comma-separated integers.
#     Returns the list of integers.
#     """
#     while True:
#         try:
#             n = int(input("How many inputs do you want to enter : "))
#             if n <= 0:
#                 print("Please enter positive number greater than 0")
#                 continue
#             break
#         except ValueError:
#             print("Invalid Input. Please Enter valid input")
    
#     while True:
#         try:
#             raw_input = input(f"Enter {n} intergers separated by comam ',' : ")
#             numbers = [int(x.strip()) for x in raw_input.split(",")]
#             if len(numbers) != n :
#                 print(f"You entered {len(numbers)} numbers. Expected {n}. Try again.")
#                 continue
#             return numbers
#         except ValueError:
#             print("Please make sure all values are valid integers, separated by commas.")




# def odd_product_checker(n):
#     for i in range(len(n)):
#         for j in range(len(n)):
#             if i != j :
#                 if (n[i] * n[j]) & 1:
#                     return True
#     return False    


# user_dict = get_user_define_list()
# print(odd_product_checker(user_dict))

# dt1 = [2, 4, 6, 8]
# dt2 = [1, 6, 4, 7, 8]
# dt3 = [1, 3, 5, 7, 9]

# print(odd_product_checker(dt1))
# print(odd_product_checker(dt2))
# print(odd_product_checker(dt3))


# """
# 149. Cube Sum of Smaller Integers

# Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified number.
# """

# def get_valid_integers(prompt:str="Enter the number : ")->tuple[int]:
#     while True:
#         n = input(prompt)
#         try:
#             n = int(n)
#             return n
#         except ValueError as ve :
#             print(f"Only value-related error: {ve}")
#         except Exception as e:
#             print("Unexpected Error : {e}")


# def get_sum_of_cubes(n=5):
#     n -=  1
#     sum = 0 
#     while n > 0:
#         sum += n ** 3 
#         n -= 1 
    
#     return sum 

# n = get_valid_integers()
# print(get_sum_of_cubes(n))

# print(get_sum_of_cubes())


# """
# 148. Max and Min Without Built-ins

# Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
# Note: Do not use built-in functions.
# """

# def get_user_dict():
#     while True:
#         try:
#             n = int(input("How many numbers you want to enters : "))
#             if n < 0:
#                 print("Enter the positive integer greater than 0")
#                 continue
#             break
#         except Exception as e:
#             print(f"An error occured {e}")
    

#     while True:
#         raw_inputs = input(f"Enter the {n} number of inputs separated by ',' : ").strip()
#         numbers = [int(i.strip()) for i in raw_inputs.split(",")] 
#         if len(numbers) != n:
#             print(f"You enter {len(numbers)} expected {n} numbers")
#             continue
#         return numbers
    

# def get_max_min(user_dict):
#     min = user_dict[0]
#     max = user_dict[0]

#     for num in user_dict:
#         if num > max :
#             max = num 
#         elif num < min:
#             min = num 
#     return min,max

    
# user_dict = get_user_dict()

# print(user_dict)

# small, large = get_max_min(user_dict)
# print(f"minimum number in user input is {small} amd large number in user input is {large}")


# """
# 147. Divisibility Tester

# Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user.
# """

# def get_user_input():
#     while True:
#         user_input = input("Enter any 2 integers separated by comma ',' : ")
#         numbers = [(int(i.strip())) for i in user_input.split(",") ]
#         if len(numbers) != 2 :
#             print("Enter 2 valid integers ")
#             continue
#         return numbers

# def check_divisiblity(m,n):

#     if m % n == 0:
#         return True
#     return False
    

# m,n = get_user_input()

# print(check_divisiblity(m,n))


    
# """
# 146. Locate Python Module Sources

# Write a Python program to find the location of Python module sources.
# """

# print("Location of python module sources : ")

# # import imp 

# # print("Location of module os is :")

# # print(imp.find_model('os'))

# import os 

# print(os.path)

# import sys
# print(sys.path)

# """
# 145. Check List, Tuple, or Set

# Write a Python program to test if a variable is a list, tuple, or set.
# """

# x = ['a', 'b', 'c', 'd']
# y = {'a', 'b', 'c', 'd'}
# z = ('tuple', False, 3.2, 1)

# if type(x) == list:
#     print('x is a list')
# elif type(x) == set:
#     print('x is a set')
# elif type(x) == tuple:
#     print('x is a tuple')
# else:
#     print('type of x is none of the list, dict or tuple')


# if type(y) == list:
#     print('y is a list')
# elif type(y) == set:
#     print('y is a set')
# elif type(y) == tuple:
#     print('y is a tuple')
# else:
#     print('type of y is none of the list, dict or tuple')


# if type(z) == list:
#     print('z is a list')
# elif type(z) == set:
#     print('z is a set')
# elif type(z) == tuple:
#     print('z is a tuple')
# else:
#     print('type of z is none of the list, dict or tuple')


# """
# 144. Variable Type Checker

# Write a Python program to check whether a variable is an integer or string.
# """

# print(isinstance(25,int) or isinstance(25,str))
# print(isinstance([25],int) or isinstance([25],str))
# print(isinstance("25",int)or isinstance("25",str))

# """
# 143. Shell Bit Mode Detector

# Write a Python program to determine if the Python shell is executing in 32-bit or 64-bit mode on the operating system.
# """

# import os 
# import sys 
# import struct
# print(struct.calcsize("p") * 8 )


# """
# 142. Consecutive Zero-One Checker

# Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False.
# Original sequence: 01010101
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# True
# Original sequence: 00
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# False
# Original sequence: 000111000111
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# True
# Original sequence: 00011100011
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# False
# """

# def test_str(string):
#     while len(string) > 0:
#         string = string.replace("01","")

#     return True  if len(string) == 0 else False


# string1 = "01010101"
# string2 = "000111000111"
# string3 = "00011100011"
# string4 = "00"

# print(test_str(string1))
# print(test_str(string2))
# print(test_str(string3))
# print(test_str(string4))


# """
# 141. Decimal to Hexadecimal

# Write a python program to convert decimal to hexadecimal.
# Sample decimal number: 30, 4
# Expected output: 1e, 04
# """

# number = int(input("Enter the decimal number : "))
# hex_codes = '0123456789ABCDEF'


# def decimal_tp_hex_calculator(number=76):
#     print("manual way")
#     result = ''
#     if number == 0:
#         result = "0" + result
#     while number > 0:
#         remainder = number % 16
#         hex_character = hex_codes[remainder]
#         result = hex_character + result
#         number //= 16
    
#     return result

# print(decimal_tp_hex_calculator(number))
# dechimal_nums = [0, 15, 30, 55, 355, 656, 896, 1125]

# print([decimal_tp_hex_calculator(num) for num in dechimal_nums])

# print("inbuilt function")

# print(hex(number)[2:])
# print([hex(num)[2:] for num in dechimal_nums])

# result = ''
# if number == 0:
#     result = "0" + result

# while number > 0:
#     remainder = number % 16 
#     hex_character = hex_codes[remainder]
#     result = hex_character + result
#     number = number // 16


# """
# 140. Binary with Leading Zeroes

# Write a Python program to convert an integer to binary that keeps leading zeros.
# Sample data : x=12
# Expected output : 00001100
# 0000001100
# """

# number = int(input("Enter the deciaml numbewr : " ))

# result = ''

# while number > 0:
#     result = str(number % 2) + result 
#     number //= 2
    
    

# result = result.zfill(32)

# print(result)


# """
# Write a code to convert a hexadecimal code to binary code 
# """

# hex_input = input("Enter the hexadecimal number : ")

# hex_codes = "0123456789ABCDEF"

# decimal = 0

# for i in range(len(hex_input)) :
#     if hex_input[i] not in hex_codes:
#         print("Invalid hexadicimal number")
    
#     value = hex_codes.index(hex_input[i])

#     decimal = value * (16 ** (len(hex_input) - 1 - i)) + decimal

# print(decimal)


# """
# 139. IP Address Validator

# Write a Python program to validate an IP address.
# """

# import socket 

# my_ip = "weger.dfhe.ergerger"
# print(dir(socket))

# try: 

#     print(socket.inet_aton(my_ip))
#     print("Valid IP")
# except socket.error:
#     print(f"Invalid IP {socket.error}")



# """ 
# 138. Boolean to Integer Converter

# Write a Python program to convert true to 1 and false to 0.
# """

# x = True
# print(int(x)) 

# y = False
# print(int(y))

# """
# 137. Extract Dictionary Pair

# Write a Python program to extract a single key-value pair from a dictionary into variables.
# """

# dict_pairs = {'Red': 'Green'}
# dict_pairs1 = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}

# (x,y), = dict_pairs.items()
# print(x,y)

# x,y = list(dict_pairs1.items())[0]
# print(x,y)
# x,y = list(dict_pairs1.items())[3]
# print(x,y)

# """
# 136. Files Only in Directory

# Write a Python program to find files and skip directories in a given directory.
# """
# import os 
# user_path = "c:/"

# for file in os.listdir(user_path):
#     path = os.path.join(user_path,file)
#     if os.path.isdir(path):
#         continue
#     print(file)


# """
# 135. Print Variable Without Spaces

# Write a Python program to print a variable without spaces between values.
# Sample value : x =30
# Expected output : Value of x is "30"
# """

# x = 30
# print(f"""Value of x is "{x}" """)

# """
# 134. Input Two Integers

# Write a Python program to input two integers on a single line.
# """

# x,y = map(int,((input("Enter any 2 number like 12,30 : ")).strip().split(",")))
# print(x,y)


# """
# 133. Program Runtime Calculator

# Write a Python program to calculate the time runs (difference between start and current time) of a program.
# """
# import time 
# from timeit import default_timer
# def timer(n):
    
#     start = time.time()
#     start1 = default_timer()
#     for i in range(n):
#         print(i)
#     total_time  = time.time() - start
#     total_time2 = default_timer() - start1
#     print(f"Time taken for execution is {total_time}")
#     print(f"Time taken for execution is {total_time2} using default timer")


# timer(5)
# timer(15)

# """
# 132. List Home Directory

# Write a Python program to list the home directory without an absolute path.

# """
# import os.path

# print(os.path)
# print(os.path.expanduser('~'))

# """
# 131. Split Variable Length String

# Write a Python program to split a variable length string into variables.
# """

# x,y,z = [123,"Alex",56.98]
# print(x,y,z)
# print(x)
# print(y)
# print(z)


# """
# 130. Double Quotes String Display

# Write a Python program that uses double quotes to display strings.
# """
# import json 

# data  = data = {'Alex': 1, 'Suresh': 2, 'Agnessa': 3}

# print(json.dumps(data))

# """
# 129. Add Leading Zeroes

# Write a Python program to add leading zeroes to a string.
# """

# str1 = "122.22"

# print(str1.ljust(10,'0'))
# print(str1.ljust(8,'0'))


# print(str1.rjust(10,'0'))
# print(str1.rjust(8,'0'))


# """
# 128. Lowercase Letters Checker

# Write a Python program to check whether lowercase letters exist in a string.
# """

# str1 = 'A8238i823acdeOUEI'

# # for letter in str1:
# #     print(letter.islower())

# print(any(ch.islower() for ch in str1))


# """
# 127. Integer Fits in 64 Bits

# Write a Python program to check whether an integer fits in 64 bits.
# """

# internal_int = 30

# if internal_int.bit_length() < 63:
#     print(internal_int.bit_length())
#     print((-2 ** 63).bit_length())

#     print((2 ** 63).bit_length())


# """
# 126. Get Module Object

# Write a Python program to get the actual module object for a given object.
# """
# from inspect import getmodule

# from math import sqrt

# print(getmodule(sqrt))



# """
# 125. Sum Collection Counts

# Write a Python program to sum all counts in a collection.
# """

# num = [2, 2, 4, 6, 6, 8, 6, 10, 4]
# print(len(num))

# """
# 124. Variable Equality Checker

# Write a Python program to check whether multiple variables have the same value.
# """
# x = 20 
# y = 20 
# z = 20

# print(x == y == z)


# """
# 123. Max and Min of Number Types

# Write a Python program to determine the largest and smallest integers, longs, and floats.
# """

# import sys 

# print(sys.float_info)
# print(sys.int_info)
# print(sys.maxsize)



# """
# 122. Empty Variable Without Deletion

# Write a Python program to empty a variable without destroying it.

# Sample data: n=20
# d = {"x":200}
# Expected Output : 0
# {}
# """

# n = 20 

# d = {"x":200}

# z = 20.11

# y = [1,2,3,4]

# print(type(n))
# print(type(d))
# print(type(z))
# print(type(y))
# print(type(n)())
# print(type(d)())
# print(type(z)())
# print(type(y)())



# """
# 121. Variable Defined Checker

# Write a Python program to determine if a variable is defined or not.
# """

# try :
#     x = 32

# except NameError:
#     print("Variable not define")
# else:
#     print("Variable is define")

# try :
#     y 
# except NameError:
#     print("Variable not define")
# else:
#     print('Variable is define ')

# """
# 120. String Formatter with Length Limit

# Write a Python program to format a specified string and limit the length of a string.
# """

# numb = 1323.345

# print(f"this is num {numb:.5f}")
# print(f"this is num {numb:.2f}")
# print(f"this is num {int(numb):b}")
# print(f"this is num {int(numb):x}")
# print(f"this is num {int(numb):o}")


# """
# 119. Round Float to Decimals

# Write a Python program to round a floating-point number to a specified number of decimal places.
# """

# # Define the order amount as a floating-point number.
# order_amt = 212.374

# # Print the total order amount with 6 decimal places.
# print('\nThe total order amount comes to %f' % order_amt)

# # Print the total order amount with 2 decimal places using string formatting.
# print('The total order amount comes to %.2f' % order_amt)

# # Print a blank line for formatting.
# print()


# """
# 118. Create Bytearray from List

# Write a Python program to create a bytearray from a list.
# """

# nums = [10, 20, 56, 35, 17, 99]

# print(type(nums))

# for num in nums:
#     print(num),print(type(num))

# nums = bytearray(nums)

# for num in nums:
#     print(num),print(type(num))


# print(type(nums))

"""
117. String Memory Location Test

Write a Python program to prove that two string variables of the same value point to the same memory location.
"""
str1 = "Python"
str2 = "Python"

print(id(str1))
print(id(str2))

print(hex(id(str1)))
print(hex(id(str2)))

print(id(str1)==id(str2))


"""
116. Print Unicode Characters

Write a Python program to print Unicode characters.
"""
str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'

str3 = '\0050\0079\0074\0068\006f\006e \0045\0078\0065\0072\0063\0069\0073\0065\0073 \002d \0077\0033\0072\0065\0073\006f\0075\0072\0063\0065'
print(str)
print(str3)

str4 = "Python Exercises - w3resource"


for char in str4:
    print(u(ord(char)))
#import base64

# base64_string
# file_bytes = base64.b64decode(base64_string)
# file_bytes1 = base64.b64decode(base64_string1)

# print(file_bytes)
# print(file_bytes1)
# print("This is header")
# header = file_bytes[:50]
# header1 = file_bytes1[:50]



# print(header)
# print(header1)



