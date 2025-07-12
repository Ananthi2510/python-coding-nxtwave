#Reads two numbers M and N , and prints a  rectangle of M rows and N columns using pluses (+)

M = int(input())
N = int(input())

counter = 1 

while counter <= M:
    print("+ " * N)
    counter = counter + 1
