#Reads three numbers
A = int(input())
B = int(input())
C = int(input())

#Checks if the sum of any numbers is always greater than 10
result = (A + B > 10) and (B + C > 10) and (A + C > 10)
print(result)
