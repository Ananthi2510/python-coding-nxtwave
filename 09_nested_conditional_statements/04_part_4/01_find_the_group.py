# reads a number and prints the group in which the given number is present. The number  is always from 1 to 10.

number = int(input())

remainder = number % 2

if remainder == 1:
    print("Group A")
else:
    print("Group B")
