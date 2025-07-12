# reads a number N and prints a Right Angled Triangle of N rows using stars (*).

number = int(input())

counter = 1

while counter <= number:
    print("*" * counter)
    counter = counter + 1
