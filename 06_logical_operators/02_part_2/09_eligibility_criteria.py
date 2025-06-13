#reads marks in maths, physics, chemistry
M = int(input())
P = int(input())
C = int(input())

#Checks if any of the conditions is satisfied
#M >=70 and P >=60 and C >=60 
#M + P + C >= 180
result = (M >= 70 and P >= 60 and C >= 60) or (M + P + C >= 180)
print(result)
