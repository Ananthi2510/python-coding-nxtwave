#Reads a two digit number
n = input()

a = int(n[0])
b = int(n[1])

#checks if the number is divisible by both the digits of the number
if N % a == 0 and N % b == 0:
    print(int(n) * 2)
else:
    print(n)
