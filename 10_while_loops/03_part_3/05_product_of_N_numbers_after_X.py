#Reads two numbers X and N , and prints the product of N numbers after X.

X = int(input())
N = int(input())

counter = 1
product = 1
while counter <= N:
    X = X + 1
    product = product * X
    
    counter = counter + 1 
print(product)
