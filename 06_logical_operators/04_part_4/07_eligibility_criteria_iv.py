#Read the marks in Maths, Physics and Chemistry
M = int(input())
P = int(input())
C = int(input())

#Check if any of the below conditons are satisfied 
#M >= 65 and P >= 50 and C >= 45 and M+P+C >= 180
#M+P >= 120 or C+P >= 110 

first_cond = (M >= 65) and (P >=50) and (C>= 45) and (M+P+C >= 180)
second_cond = (M+P >= 120) or (C+P >= 110)

result = first_cond and second_cond
print(result)
