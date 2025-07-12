# reads a number N and prints a square of N rows and N columns using numbers starting from 1.

number = int(input())

counter = 1
while counter <= number:
    row = str(counter) * number
    print(row)
    counter = counter + 1
