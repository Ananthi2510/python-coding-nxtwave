#reads the rank R of a student and checks if the rank is less than or equal to 3 or 10.

rank = int(input())

is_less_than_or_equal_10 = rank <= 10
is_less_than_or_equal_3 = rank <= 3

if is_less_than_or_equal_10:
    if is_less_than_or_equal_3:
        print("One of Top 3")
    else:
        print("Not Top 3 but One of Top 10")
