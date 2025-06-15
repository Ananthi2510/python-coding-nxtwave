#reads three sides of a triangle
A = int(input())
B = int(input())
C = int(input())

#check if sum of any two sides of the triangle is always greater than the third side
result = (A + B > C) and (B + C > A) and (A + C > B)
print(result)
