#Reads two three digit numbers
A = input()
B = input()

a = int(A[0])
b = int(B[2])

#checks if the first digit of A is less than the last digit of B
result = a < b 
print(result)
