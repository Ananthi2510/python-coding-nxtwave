#Reads a percentage P and a number N 
P = int(input())
N = int(input())

#Checks if the P percentage of 500 is equal to the number N
value = (P / 100) * 500
result = value == N

print(result)
