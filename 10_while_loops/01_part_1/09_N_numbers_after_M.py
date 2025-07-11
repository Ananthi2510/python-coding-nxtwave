# reads two numbers M and N and prints N numbers after M.

m = int(input())
n = int(input())

counter = 0

while counter < n:
    m = m + 1
    print(m)
    counter = counter + 1
