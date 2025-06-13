#reads a three digit number 
A = input()

first_digit = int(A[0])
second_digit = int(A[1])
third_digit = int(A[2])

#checks if a given three-digit number contains the digit 0
result = (first_digit == 0) or (second_digit == 0) or (third_digit == 0)
print(result)
