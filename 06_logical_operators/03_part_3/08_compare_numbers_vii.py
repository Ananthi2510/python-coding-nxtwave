#Reads a four digit numnber
number = input()


length = len(number)

first_two_digits = int(number[:2])
last_two_digits = int(number[length - 2:])

is_nineteen = first_two_digits == 19
is_between_30_and_60 = (last_two_digits > 30) and (last_two_digits < 60)

#checks if the first two digits of the number are 19 and the last two digits of the number are between 30 and 60.
result = is_nineteen and is_between_30_and_60
print(result)
