#Reads two numbers
a = int(input())
b = int(input())

#checks if one of the below conditions is satisfied
#One of A and B is equal to 6.
#The sum of A and B is equal to 6.

if (a == 6 or b == 6) or (a + b == 6) or (a - b == 6 or b - a == 6):
    print("Lucky")
else:
    print("Not Lucky")
