n = int(input())
remainder_1 = n % 4
remainder_2 = n % 5
if remainder_1 > remainder_2:
    print(remainder_1)
else:
    print(remainder_2)
