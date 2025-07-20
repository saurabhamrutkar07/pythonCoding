""" Iterationg over list """

color_list = ['Red', 'Green','Blue','Black']
for c in color_list:
    print(c)


""" Python for loop and range() function """

""" The range() function returns a list of consecutive integers. The function has one, two or three parameters where last two parameters are optional. It is widely used in for loops. """

for a in range(4):
    print(a)


for a in range(2,7):
    print(a)


for a in range(2,19,5):
    print(a)


""" Python for loop: Iterating over different Data Structures """

numbers = (1,2,3,4,5,6,7,8,9)
count_odd = 0 
count_even = 0

for i in numbers:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Numbers of even numbers : ",count_even)
print("Numbers of odd numbers : ",count_odd)


""" Example: Iterating over list """

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]

for item in datalist:
    print(f"type of {item} is {type(item)}")


""" Example: Iterating over dictionary """

color = {"c1": "Red", "c2": "Green", "c3": "Orange"}

for key in color:
    print(key)


for value in color.values():
    print(value)