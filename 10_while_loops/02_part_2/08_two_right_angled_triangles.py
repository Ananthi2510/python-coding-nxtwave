#Reads a number N and prints two Right angled triangles of N rows , using numbers starting from 1

N = int(input()) 
counter = 1 

while counter <= N:
    print(str(counter) * counter)
    counter = counter + 1

counter = 1
while counter <= N:
    print(str(counter) * counter)
    counter = counter + 1
