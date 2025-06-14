#read the marks in Maths (M), Physics (P), and Chemistry (C)

M = int(input())
P = int(input())
C = int(input())

#Check if any sum of pairs is greater than or equal to 100
is_sum_greater_or_equal = (M + P >= 100) or (P + C >= 100) or (C + M >= 100)

#Check if the total marks are greater than or equal to 180
is_total_marks_greater_or_equal = (M + P +C) >= 180

#Check if all the conditions are satisfied
result = is_sum_greater_or_equal and is_total_marks_greater_or_equal
print(result)
