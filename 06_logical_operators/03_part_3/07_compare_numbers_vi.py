number = input()

first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])

#checks if each digit is greater than 4 or the first digit is equal to 6
is_greater_than = (first_digit > 4) and (second_digit > 4) and (third_digit > 4)
is_first_digit_six = first_digit == 6

result = is_greater_than or is_first_digit_six
print(result)
