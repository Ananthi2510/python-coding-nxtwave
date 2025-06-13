#Reads two numbers
first_number = int(input())
second_number = int(input())

#find sum and product 
sum = first_number + second_number
product = first_number * second_number 

#checks if both the sum and the product of two numbers have less than three digits
sum = str(sum)
sum_digits = len(sum)
is_sum_length_less_than_three = sum_digits < 3 

product = str(product)
product_digits = len(sum)
is_product_length_less_than_three = product_digits < 3 

result = (is_sum_length_less_than_three) and (is_product_length_less_than_three) 
print(result)
