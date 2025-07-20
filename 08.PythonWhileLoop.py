""" While Loop """

""" Loops are used to repeatedly execute a block of program statements. The basic loop structure in Python is while loop. """


""" 
The while loop runs as long as the expression (condition) evaluates to True and execute the program block. The condition is checked every time at the beginning of the loop and the first time when the expression evaluates to False, the loop stops without executing any remaining statement(s). 

"""

x = 0 

while x < 5:
    print(x)
    x +=1 


""" One thing we should remember that a while loop tests its condition before the body of the loop (block of program statements) is executed. If the initial test returns false, the body is not executed at all. """

x = 10 
while x < 5:
    print(x)
    x += 1


""" While loop and else statement """

""" 
There is a structural similarity between while and else statement. Both have a block of statement(s) which is only executed when the condition is true. The difference is that block belongs to if statement executes once whereas block belongs to while statement executes repeatedly.
"""

x = 0 
s = 0 

while x < 10 :
    s += x 
    x += 1
else:
    print("The sum of first 9 integers : ", s)



"""while loop with if-else and break statement"""

x = 1 
s = 0 

while x < 10 : 
    s += x 
    x += 1 
    if x == 5:
        break
else:
    print("The sum of first 9 integers : ", s )
print("The sum of ", x," number is : ",s)  