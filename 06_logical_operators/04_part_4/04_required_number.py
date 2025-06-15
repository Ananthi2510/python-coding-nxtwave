#reads a number N 
N = int(input())
n = str(N)

#checks if the number N is between 50 and 100 or if the first digit of N is equal to 7.
print((N > 50 and N < 100) or n[0] == "7")
