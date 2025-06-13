a = input()

is_above = int(a) > 25

first_digit = a[0]
second_digit = a[1]

first_digit = int(first_digit)
second_digit = int(second_digit)

is_greater = first_digit > second_digit

result = is_above and is_greater
print(result)
