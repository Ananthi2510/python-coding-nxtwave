A = int(input())
B = int(input())

is_sum_negative = (A + B) < 0
is_product_negative = (A * B) < 0

#check if sum of A and B is negative or product of A and B is negative
result = is_sum_negative or is_product_negative 
print(result)
