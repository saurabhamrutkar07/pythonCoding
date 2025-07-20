""" Vatiable is nameed memory allocation where data can be stored
    Value is a data stored in valriable which can be string, numerica value


    Variable created when they first assign a value 
    They must be assign before referred 
    value stored in variable can be accessed or update later 
    no decalration required before using a variable 
    python manages memory allocation based on type of variable 

    Rules : 
        must begin with letter or _ underscore
        subsequent charaters can be letter, underscore or number 
        Case sensitive : age, AGE , Age can be considered as different variables
        can be of any resonable length 
        reserved words can not be used as variable names

    Good variable naming practice : 
        Choose meaningful names, such as roll_no, which is clearer than rn.
        Avoid unnecessarily long variable names (e.g., Roll_no_of_a_student is too long).
        Be consistent in your naming convention: roll_no or RollNo, but not both.
        Start variable names with an underscore (_) when you need a special case or private variables.
    
 """


""" Python assignment statement """

item_name = "Computer"
item_quantity = 10
item_value = 1000.23

print(item_name)
print(item_quantity)
print(item_value)



""" Multiple assignment """

x = y = z = 1
print(x)
print(y)
print(z)


x,y,z = 1,2,'abc'

print(x)
print(y)
print(z)

""" We can reuse the variable name by assigning them new variable value """
x = 100 
print(x)
x = "Python"
print(x)

""" Other ways to declare values """

five_millions = 5_000_000
print(five_millions)

samll_int = .35
print(samll_int)

c_thousand = 10e3
print(c_thousand)

""" Swaping of variables """

x = 10 
y = 20 
print(x)
print(y)

x,y = y,x

print(x)
print(y)


""" Local and global variables in python """

"""   
Global variables are accessible throughout the entire program, even within functions.
Local variables are defined within a function and cannot be accessed outside it.
A variable is assumed to be local unless explicitly declared as global using the global keyword.
"""

var1 = "Python"

def func1():
    var1 = "PHP"
    print("Inside func1() var1 = ", var1)

def func2():
    print("Inside func2() var1 = ", var1)


func1()
func2()


"""   
You can use a global variable in other functions by declaring it as global keyword
"""

def func1():
    global var3
    var3 = "PHP"
    print("Inside func1() var3 = ", var3)

def func2():
    print("Inside func2() var3 = ", var3)


func1()
func2()