#Read the marks in Maths, Physics and Chemistry
M = int(input())
P = int(input())
C = int(input())

#Check if both the conditons are satisfied 
#M >= 35 and P >= 35 and C >= 35
#M + P >=90 or P+C >=90 and M+C >=90
is_greater = (M >= 35) and (P >= 35) and (C >= 35)
is_sum_greater = (M + P >= 90) or (P + C >= 90) or (M + C >= 90)

result = is_greater and is_sum_greater
print(result)
