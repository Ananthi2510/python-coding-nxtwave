#Reads an age A and guardian status S
A = int(input())
S = input()

#checks if the age is between 12 and 60 or if the guardian status is equal to yes
result = (A > 12 and A < 60) or (S == "yes")
print(result)
