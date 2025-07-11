#Reads N numbers as inputs and print the product of the given N Numbers


N = int(input())
counter = 1 
product = 1
while counter <= N: 
    n1 = int(input())
    product = product * n1 
    counter = counter + 1 
print(product)
