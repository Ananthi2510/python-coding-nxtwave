#Reads a number N and prints a square of N rows and N columns using stars (*)

N = int(input())
counter = 1 

while counter <= N:
    print("* " * N)
    counter = counter + 1 
