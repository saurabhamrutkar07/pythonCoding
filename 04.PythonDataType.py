""" Numbers """
""" 
Pytohn has 3 distince number types 
Integer : Without factorial part 
floating points : with decimal points
Complex numbers : containing real and imaginary part e.g. (A + Bi)

"""


a = 1234
b = -4567
c = 0 
g = 1.03 
h = -11.03 
i = .34
j = 2.12e-10
k = 5e220

print(type(a))
print(type(b))
print(type(c))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))


x = 8 
y = 7 

print(x + y)
print(x - y)
print(x * y)
print(x / y)

""" Exponential """
print(4**3)
print(3**4)

""" Integer Division """
print(12/3)
print(64//4)
print(15//3)

""" Remainder """

print(15 % 4)

""" Complex number """

x = complex(1,2)
print(x)

z = 1 + 2j

print(type(z))


"""  
Self assignment operator 
"""

count = 0 

count += 2 

print(count)

count -= 2 

print(count)

count += 2 

print(count)

count *= 4 

print(count)

count **= 4 

print(count)

count /= 4 

print(count)

count //= 4 

print(count)

print(15//2)

"""   Order of operation """

print((3 + 12)/3)

print(15/(3+2))

""" Boolean """

x = True

y = False 

print(type(x))
print(type(y))


""" String """

string_1 = "Python Tutorial"

print(string_1[0]) # Print first character 
print(string_1[-15]) # Print first character 
print(string_1[-1]) # Print last character 
print(string_1[14]) # Print last character 
print(string_1[4]) # Print fourth character 


"""   
Strings are immutable
Strings are immutable character sets. Once a string is generated,
you can not change any character within the string. See the following statements
"""

""" in operator in string """

print("Z" in string_1)
print("P" in string_1)
print("Tut" in string_1)


""" Conversion """

print(float("4.5"))
print(int("25"))
print(int(5.635))
print(float(6))
print(float(False))
print(str(True))
print(bool(0))
print(bool('Hello World'))
print(bool(223.5))



""" Tuple """
"""  
A tuple is a container which holds a series of comma separated values between parenthesis 
Tuples are immutable and can hold mix data types 
"""


tup1 = (0,1,-1,12,212.23,100)
print(type(tup1))
print(tup1)

tup2 = ('Red', 'Black', 2000, 'White')
print(tup2)

tup3 = "a1","b1","c1","d1"

print(type(tup3))
print(tup3)

empty_tuple = tuple()
single_tup = (100,)
print(single_tup) 
print(type(single_tup))
print(empty_tuple)
print(type(empty_tuple))

""" Elements of a tuple are indexed like other sequences. The tuple indices start at 0. """

print(tup2[0])
print(tup2[3])


""" Tuples are mutable means values are unchangable """

""" Slicing s tuple """

print(tup2[0:2])
print(tup2[1:2])
print(tup2[1:-2])
print(tup2[:3])



""" Using + and * operator in tuple """

""" Use + operator to create a new tuple that concatnation of tuples and use * repeat the tuple """

tup1 = (1,2,3)
tup2 = (4,5,6)
tup3 = (7,8,9)

print(tup1 + tup2 + tup3)

print(tup1 * 4)


""" Lists """

""" Creating lists """

""" A list is a container which holds comma-separated values (items or elements) between square brackets where Items or elements need not all have the same type. """

my_lists = [5,12,13,14]
print(my_lists)

my_lists2 = ['red', 'blue', 'black', 'white']

print(my_lists2)


my_lists3 = ['red', 12, 112.12]

print(my_lists3)

""" A list without any element is called an empty list. """

my_list = []

print(my_list)


""" List Indices """

""" List indices work the same way as string indices, list indices start at 0. If an index has a positive value it counts from the beginning and similarly it counts backward if the index has a negative value. As positive integers are used to index from the left end and negative integers are used to index from the right end, so every item of a list gives two alternatives indices. Let create a list called color_list with four items.
color_list=["RED", "Blue", "Green", "Black"] """


color_list = ["red", 'blue', 'green', 'black']
print(color_list)

print(color_list[0],print(color_list[3]))

print(color_list[-1])

""" List slices """

""" Lists can be sliced like strings and other sequences. The syntax of list slices is easy :
sliced_list = List_Name[startIndex:endIndex]
This refers to the items of a list starting at index startIndex and stopping just before index endIndex. The default values for list are 0 (startIndex) and the end (endIndex) of the list. If you omit both indices, the slice makes a copy of the original list. """


print(color_list[0:2])

print(color_list[1:2])

print(color_list[1:-2])

print(color_list[:3])

print(color_list[:])

""" Lists are mutable """

""" Items in the list are mutable i.e. after creating a list you can change any item in the list. """

print(color_list[0])

color_list[0] = "white"

print(color_list)

print(color_list[0])


""" Using + and * operator in list """

""" Use + operator to create a new list that is a concatenation of two lists and use * operator to repeat a list.  """

color_list1 = ["white",'yellow']
color_list2 = ['red','blue']
color_list3 = ['green','black']

print(color_list1 + color_list2 + color_list3)

numbers = [1,2,3,4]
print(numbers[1]*4)
print(numbers * 4)


""" Sets """

""" A set is an unordered collection of unique elements. Basic uses include dealing with set theory (which support mathematical operations like union, intersection, difference, and symmetric difference) or eliminating duplicate entries. """


a = [1,2,1,3,0,0,4,7,8,6]
b = [5,5,7,8,7,9,6,1,1,2]

s1 = set(a)
s2 = set(b)
print(s1)
print(s2)

print(s1 - s2) # numbers in s1 but not in s2


print(s1 | s2) # unique elements after combining both the sets

print( s1 & s2) # number present in both s1 and s2 

print( s1 ^ s2) 


""" Dictonary """

""" Python dictionary is a container of the unordered set of objects like lists.
The objects are surrounded by curly braces { }. 
The items in a dictionary are a comma-separated list of key:value pairs where keys and values are Python data type. 
Each object or value accessed by key and keys are unique in the dictionary. 
As keys are used for indexing, they must be the immutable type (string, number, or tuple). 
You can create an empty dictionary using empty curly braces """


pd = {"class": "V", "section": "A", "roll_no": 12}

print(pd)
print(pd['class'])
print(pd['section'])
print(pd['roll_no'])


""" None """

""" This type has a single value. There is a single object with this value. This object is accessed through the built-in name None. It is used to signify the absence of a value in many situations, e.g., it is returned from functions that don't explicitly return anything. Its truth value is false. """




