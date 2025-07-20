""" 
Parameters : 

step : Specifies the separator between values. Default its single space. 

end : Specifies the string to be appended at the end of the output. Default is new line

file : Defines the output destination Default is sys.stdout. Use sys.stderr for errors 

flush : If True forcibly fluches the output buffer

"""

""" 
Example with sep and end 
"""

print("Python","is","fun", sep="-")
print("Hello", end=", ")
print("World")



""" Advasnce String Formaatting """

name = "Tom"
age = 25

print(f"Hello {name}, you are {age} years old")


""" Using ().format"""

name = "Tom"
age = 25

print("Hello {}, you are {} years old.".format(name,age))


""" Using % operator """

name = 'Tom'
age = 25

print("Hello %s, your are %d years old." % (name,age))


""" Working with Quotes in String """

""" 
Single quote for nnormal string 'Hello'

Double Quote : It is useful when string has ' single quote in it "Python's Simplicity"

Triple Quote : Allows multiline string and embedded quote

"""

print("""Pyrhon is versatile 
It's also popular """)


""" Veriable use """

val1 = "Wel"
print(val1,'come')

val1 = 'Welcome'
val2 = 'Python'
print(val1,val2)

""" String Concatination """

val1 = 'Python'
val2 = ':'

print("Welcome"+ val1 + val2)

""" Using a string """

""" %s is used to refer to a variable which contains a string """

str1 = "Python"
print("Welcome %s" %str1)


"""  
Other data types 

%d  for int 

%s for string 

%e for exponential 

%f for float

%o for Octal

%x for Hexadecimal
"""

""" Using integer """

print("Actual number is %d" %15)

""" Using as exponential """

print("Exponential equivalent of number = %e" %15)

""" Using float """
print("Float of the number %f" %15)

""" Using octal """
print("Octal Equivalent of the number = %o" %15)

""" Using  as hexadecimal """
print("Hexadecimal of number = %x" %15)


""" Using multiple Variables """

val1 = 'World'
val2 = ':'

print('Python %s %s'%(val1,val2))


""" Repeating characters """
print("#" * 10)

""" Other way of print statement """

print("Welcome to Python %s" %'language')

""" Line Break """
print("Sunday \nMonday \nTuesday \nWednesday \nThursday\nFriday\nSaturday")

""" Multiple Times """
print("-w3r" * 5)

""" using tab """

print("""Language : 
      \t 1.Python 
      \t 2.java \n\t 3.JavaScript""")