#reads two numbers M and N, and prints a Rectangle of M rows and N columns using stars (*).

rows = int(input())
columns = int(input())

counter = 0
while counter < rows:
    print("*" * columns)
    counter = counter + 1
