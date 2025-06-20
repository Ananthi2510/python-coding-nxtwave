#Reads a two digit number
N = int(input())
n = str(N)
a = int(n[0])
b = int(n[1])

#Checks if any of the conditions are satisfied
#the number is divisible by 9 
#one of the digits of the number is equal to 9

if (N % 9 == 0) or (a == 9 or b == 9):
    print("Lucky Number")
else:
    print("Unlucky Number")
