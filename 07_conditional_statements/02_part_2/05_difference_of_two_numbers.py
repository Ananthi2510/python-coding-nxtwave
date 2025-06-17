#Reads three numbers
A = int(input())
B = int(input())
C = int(input())

#Checks if the difference between any two numbers is always  less than 25
if A - B < 25 and B - C < 25 and C - A < 25:
    print("Difference is less than 25")
else:
    print("Difference is not less than 25")
