#Reads two numbers M and N , and prints a Rectangle of M rows and N columns using the numbers from 1.
#There is a space after every number

M = int(input())
N = int(input())
counter = 1 

while counter <= M:
    s = str(counter) + " "
    print(s * N)
    counter = counter + 1
