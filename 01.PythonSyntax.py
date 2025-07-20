"""
Python Line Structure
"""

x = 1
if x > 0 :
    print("These three lines are Physical/Logical lines")



"""
Comments in python 
"""
x = 1
# internal value of x is 1 
if x > 0 :
    print("These are two comments") # print a string.





""" 
Joining two lines  
"""

u = 0
v = 1
w = 2
x = 3
y = 4
z = 5

if u == 0 and v > 0 \
    and w > 1 and x > 2 \
    and y > 3 and z > 4 :
        print("This is example of line joining")


""" 
Multiple Statement on single line 
"""

# We can write multiple statement on single line using ';' this separator

print("Statement1")
print("Statement2")
# We can write the above statement in single line
print("Statement1"); print("Statement2")


""" Indentation """

x = 1 
if x > 0 :
 print("This statement has a single space Indentation")
 
if x > 0:
    print("This statement has single tab indentation")

if x > 0:
     print('This statement has tab space and single space indentation') 


""" Python Coding Style PEP8"""

""" 
Indentation : Use 4 space per indentation avoid tabs 
Line lenght : Max 79 chars better for small screen 
Blank Line : 
    Separate top-levle functions and class definations with 2 blank lines 
    Separate metohs inside class with 1 blank line 
Inline comment : Use inline comment sparigly and make sure they are complete sentences
White Space : Add white space after comma and operators to improve reability   
"""

