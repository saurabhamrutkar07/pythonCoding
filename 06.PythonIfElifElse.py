""" If statement """

""" The Python if statement is similar to other programming languages. It executes a block of statements conditionally, based on a Boolean expression. """


""" if else statement """

""" In Python, the if..else statement has two blocks: one for when the condition is True and another for when the condition is False. """

a = 10 
if a > 10 :
    print("Value is greater than 10 ")
else:
    print("Value of a is 10")


""" if elif else statement """

""" When there are multiple conditions to check, you can use the elif clause (short for "else if"). Python evaluates each condition one by one until it finds one that is True. If none are True, the else block is executed. """


var1 = 1 + 2j

if type(var1) == int :
    print("Type of variable is Intiger")

elif type(var1) == float:
    print("Type of variable is Float")

elif type(var1) == complex:
    print("Type of variable is Complex")

elif type(var1) == bool:
    print("Type of variable is Bool")

elif type(var1) == str : 
    print("Type of variable is String")

elif type(var1) == tuple :
    print("Type of variable is Tuple")

elif type(var1) == dict :
    print("Type of variable is Dictionary")

elif type(var1) == list :
    print("Type of variable is List")
else:
    print("Type of variable is Unknown")


""" Nested if else statement """

""" You can nest if statements inside each other to check multiple conditions sequentially. The outer if is evaluated first, and if it’s True, the inner if or else block is evaluated. """

age = 38 

if age >= 11 :
    print("You are eligible to watch football match")
    if age <= 12 or age >= 60 :
        print("Ticket price is $12")
    else:
        print("Ticket price is $20")
else:
    print("You are not eligible to watch football match") 


""" Use of and operator in if statement """

x = False
y = True

if x and y :
    print("Both x and y are true")
else:
    print("x is false or y is false or both x and y are false ")


""" Use of in operator in if statement """

s = "jQuery"

l = ['JavaScript', 'jQuery', 'ZinoUI']

if s in l :
    print(s + ' Tutorial')

# This is equivalent to :

if s == 'JavaScript' or s == 'jQuery' or s == 'ZinoUI':
    print(s + ' Tutorial')


""" if else in single line of code """

n = 150
print(n)

result = n * 7 if n > 500 else n / 7 

print(result)

""" Define a negative if """

x = 20 

print(x)

if not x == 50 :
    print("the value of x is different fron 50")
else :
    print("the value of x is equal to 50")