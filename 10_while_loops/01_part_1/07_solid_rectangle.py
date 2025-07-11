#Reads two integers M and N, and prints a solid rectangle pattern of M rows and N columns using the asterisk character (*)

m = int(input())
n = int(input())

counter = 0
while counter < rows:
    print("* " * columns)
    counter = counter + 1
