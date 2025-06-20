#Reads a two digit number
N = int(input())
n = str(N)
a = int(n[0])
b = int(n[1])

#Checks if any of the given conditons is satisfied
#The sum of digits of the number is equal to 7 
#one of the digits is equal to 7
#the number is divisible by 7


if (a + b == 7) or (a == 7 or b == 7) or (N % 7 == 0):
    print("Special Number")
else:
    print("Normal Number")
