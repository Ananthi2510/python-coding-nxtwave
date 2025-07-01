# reads a number  and checks if it is divisible by 5 and 10

number  = int(input())

is_divisible_by_10 = (number % 10 == 0)
is_divisible_by_5 = (number % 5 == 0)

if is_divisible_by_10:
    print("Divisible by 10")
elif is_divisible_by_5:
    print("Divisible by 5")
else:
    print("Not Divisible by 10 or 5")
