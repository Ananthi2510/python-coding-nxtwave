#Reads two numbers
A = int(input())
B = int(input())

#Check if any of the conditions is satisfied
#sum of A and B is less than 10
#difference between A and B is less than 10
#A is between 5 and 30

print((A + B < 10) or (A - B < 10) or (A > 5 and A < 30))
