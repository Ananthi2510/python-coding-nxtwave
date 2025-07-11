#Reads two numbers M and N, and prints the sum of N numbers from M

M = int(input())
N = int(input())
sum = 0
counter = 1 

while counter <= N:
    sum = sum + M 
    counter = counter + 1
    M = M + 1
print(sum)
