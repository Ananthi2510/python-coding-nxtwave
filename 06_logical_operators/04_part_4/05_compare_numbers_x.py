#reads two numbers A and B 
A = int(input())
B = int(input())

#checks if both the conditions is satisfied 
#one of A and B is less than 20 
#one of A and B is greater than 30

is_less_than = (A < 20) or (B < 20) 
is_greater_than = (A > 30) or (B > 30)

result = is_less_than and is_greater_than
print((result)
