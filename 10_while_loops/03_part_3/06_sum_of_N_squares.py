#Reads a number N and prints the sum of squares of N numbers starting from 1.

N = int(input())
counter = 1 
sum = 0
while counter <= N:
    sum = sum + (counter ** 2)
    counter = counter + 1 
print(sum)
