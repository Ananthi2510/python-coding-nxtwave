#Given an integer N, write a program which reads N inputs and prints them.

N = int(input())

counter = 0
while counter < N:
    number = int(input())
    print(number)
    counter = (counter + 1)
