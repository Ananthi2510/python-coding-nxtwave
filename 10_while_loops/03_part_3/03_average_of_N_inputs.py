#Reads a N inputs and prints the average of the N inputs

N = int(input())
counter = 1 
sum = 0 

while counter <= N:
    n = int(input())
    sum = sum + n
    counter = counter + 1 
    
print(sum / N)
