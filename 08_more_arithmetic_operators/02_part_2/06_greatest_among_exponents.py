a = int(input())
b = int(input())

a_power_b = a ** b
b_power_a = b ** a

is_greater = a_power_b > b_power_a

if is_greater:
    print(a_power_b)
else:
    print(b_power_a)
