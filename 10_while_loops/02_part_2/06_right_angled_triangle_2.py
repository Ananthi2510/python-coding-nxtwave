#Reads a number and prints a right angled triangle of N rows using numbers starting from 1.


N = int(input())
counter = 1

while counter <= N:
    print((str(counter) + " ") * counter)
    counter = counter + 1
