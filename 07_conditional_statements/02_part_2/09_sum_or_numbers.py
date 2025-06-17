#Reads two numbers
a = int(input())
b = int(input())

#checks if one of the below conditions is satisfied.
#One of A and B is less than 20.
#The sum of A and B is between 30 and 50.

if (a < 20 or b < 20) or (30 < a + b < 50):
    print(a + b)
else:
    print(a)
    print(b)
