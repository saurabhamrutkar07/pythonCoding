""" Operators and Operands """

""" c = a + b  """

""" Here a and b are called operands and + is called operator """

x = 14 
y = 5 


""" Python arithmatic Operators """
print(x + y)
print( x - y)
print( x * y)
print(x / y)  # returns division woth float 
print( x // y) # returns division with int 
print( x % y) # returns reminder
print( x ** y) # returns raised to power of base


""" Python Comparison Operators """

x = 12
y = 15


x == y  #vTests x and y are equal or not 
x != y  # Tests x is exactly equal or not to y 
x > y  # Tests x is greater than y 
x < y  # Tests x is less than y 
x >= y # Tests x greater than or equal to y or not 
x <= y # Tests x less than or equal or not to y 

""" and or not """

"""   
and x and y returns true if x and y are true 

or x or y returns true if either x or y is true

not returns true if x not equal to y 
"""


x = 12 

y = 15 

print( x > 10 and y > 10)

print(x > 14 or y > 14)

print(not (x > 10 and y > 10))



""" Python assignment operator """

x = 12 
y = 7 

x += y 

print(x)

x -= y 
print(x)

x *= y 
print(x)

x /= y
print(x)

x %= y 
print(x)

x **=y 
print(x) 

x //=y 
print(x)



""" Python bitwise operator """

"""    

& and  x & y  bits that are set in both x and y 

| or x | y bits that are set in eother x or y 

^ XOR  x ^ y  bits that are set in x or y but not in both 
~ not equal to  ~x  bits that are set in x are not set 

<< shift left  x << y  shits the bits of x, y steps to left 

>> shift right x >> y shits the bits of x , y steps to right

"""
