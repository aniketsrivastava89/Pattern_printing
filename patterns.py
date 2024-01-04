 #   1    Increasing order traingle


n=int(input("Enter a number: "))
for i in range (n):
    for j in range(i+1):
        print("*",end=" ")
    print() 


#   2        decreaing order traingle


n=int(input("Enter a number: "))
for i in range (n):
    for j in range(i,n):
        print('*',end=" ")
    print()   


#       3        # Right side triangle 

n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end='')
    for j in range(i+1):
        print("*", end='')
    print()      

#                      right triangle star pattern

n=5
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print()      

# hill pattern in incrrasing order 

n=int(input("enter a number: "))
for i in range (n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range (i):
        print("*",end=" ")
    for j in range (i+1):
        print("*",end=" ")
    print()

