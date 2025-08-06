#class Patterns():
    




n = int(input("Enter the integer greater than 2: "))


# right_align_right_angle_triange
print("1")
print("right_align_right_angle_triange")
for i in range (1,n+1):
    print((" " * (n - i)) + ("*" * i))

print("2")
# left_align_right_angle_triange
print("left_align_right_angle_triange")
for i in range (1,n+1):
    print("*" * i)

print("3")
# center perymid 
print("center perymid")
for i in range(1,n+1):
    print((" " * (n - i)) + ("* " * i))

print("4")
# inverted_right_aligned_triangle
print("inverted_right_aligned_triangle")
for i in range (n,0,-1):
    print( " " * (n - i) + ("*" * i))



print("5")
# inverted_left_aligned_triangle

print("inverted_left_aligned_triangle")

for i in range(n,0,-1):
    print("*" * i)


print("6")
# right_align_hollow_right_angle_triange
print("right_align_hollow_right_angle_triange")

for i in range(1,n+1):
    if i in [1,2,n]:
        print(" " * (n - i) + "*" * i)
    else:
        print((" " *( n - i)) + "*" + " " *(i - 2) + "*")

print("7")
# left_align_hollow_right_angle_triange
print("left_align_hollow_right_angle_triange")

for i in range(1,n+1):
    pass
    if i in [1,2,n]:
        print("*" * i )
    else:
        print("*" + " " * (i - 2) + "*")

print("8")
# Hollow triangle
print("hollow triangle")

for i in range(1,n+1):
    if i in [1,2,n]:
        print( " " * (n - i) +"* " * i)
    else:
        print(" " * (n - i) + "* " + "  " * (i - 2) + "* ")

print("9")
# hollow inverted triangle 
print("Hollow inverted trainagel : ")

for i in range(n,0,-1):
    if i in [1,2,n]:
        print( " " * (n - i) + "* " * i )
    else:
        print(" " * (n - i) + "* " + "  " * (i - 2) + "* ")

print("10")
# pyramid without spaces or half diamond
print("pyramid without spaces or half diamond")

for i in range (1,n * 2):
    if i <= n:
        print("*" * i)
    else:
        print("*" * (2 * n - i))


print("11")
# another half daimond

for i in range(1,2* n):
    if i <= n:
        print(" " * (n - i)  +"*" * i)
    else:
        print( " " * (i - n) +"*" * (2 * n - i))

print("12")
# full daimond
print("full daimond")

for i in range(1,n * 2):
    if i <= n :
        print(" " * (n - i) + "* " * i)
    else:
        print(" " * (i - n) +"* " * (2 * n - i) )


# hollow diamond 
print("13")
print("hollow daimond")


for i in range(1,n*2):
    if i in [1,2]:
        print(" " * (n - i) + "* " * i)
    elif i  <= n:
        print(" " * (n - i) + "* " + "  " * (i - 2) + "*")
    elif i > n  and i != (2 * n - 1):
        print(" " * (i - n) + "* " + "  " * ((2*n - i - 2))  + "* ")
    else:
        print(" " * (i - n) + "* ")

    


print("Assignments")
print("This is 1")
print("left_align_right_angle_triange")
for i in range (1,n+1):
    print("*" * i)

# inverted_left_aligned_triangle
print("This is 2")
print("inverted_left_aligned_triangle")

for i in range(n+1,0,-1):
    print("*" * i)


print("This is 3")
print("left_align_right_angle_triange with numbers")

for i in range(n + 1):
    print(str(i) * i, end=" ")
    print()
    # for j in range(1,i+1):
    #     print(i, end=" ")
    # print("")

print("This is 4")

for i in range(1,n+1):
    print(str(i) * (n + 1 - i), end=" ")
    print()


print("This is 5")

for i in range(1,n+1):
    print(str(n + 1 - i) * i)


print("This is 6")

for i in range(n,0,-1):
    print(str(i) * i, end=" ")
    print()

print("This is 7")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(str(j) , end=" ")
    print()
    
print("This is 8")    
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()


print("This is 9")

for i in range(1,n+1):
    for j in range(i,0,-1):
        print(str(j), end=" ")
    print()


print("This is 10")

for i in range(1,n+1):
    for j in range(i,n+1):
        print(str(j), end=" ")
    print()

print("This is 11")
for i in range(1,n+1):
    for j in range(n,n-i,-1):
        print(str(j),end=" ")
    
    print()


print("This is 12")

for i in range(n,0,-1):
    for j in range(n,n-i,-1):
        print(j, end=' ')
    print()

    
print("This is 13")

for i in range(1,n+1,1):
    for j in range(n+1-i,n+1,1):
        print(j,end=" ")
    
    print()





# for i in range(n,0,-1):
#     print(str(i) * i , end=" ")
#     print()
