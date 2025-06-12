#Reads a two digit number
N = input()

A = int(N[0])
B = int(N[1])

#checks if the sum of the digits greater than 7
result = A+B > 7

print(result)
