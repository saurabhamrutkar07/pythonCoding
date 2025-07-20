""" Break Statement """

""" 
The break statement is used to exit a for or a while loop. The purpose of this statement is to end the execution of the loop (for or while) immediately and the program control goes to the statement after the last statement of the loop. If there is an optional else statement in while or for loop it skips the optional clause also. 

"""

numbers = (1,2,3,4,5,6,7,8,9)
num_sum = 0 
count = 0 

for x in numbers:
    num_sum += x 
    count += 1
    if count == 5:
        break

print(f"Sum of first {count} is : {num_sum}")


""" Break in while loop """

num_sum = 0 
count = 0 

while (count < 10):
    num_sum += count
    count += 1
    print("This is while loop")
    if count == 5:
        break 
print("Sum of first ", count, " integers is : ",num_sum) 


""" Contine Statement """


""" 
The continue statement is used in a while or for loop to take the control to the top of the loop without executing the rest statements inside the loop.  
Contine is used to skip the particular condition

"""


for x in range(7):
    if x == 3 or x == 6 :
        continue
    print(x)

