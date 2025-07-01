#to print the greatest among the three numbers

first_number = int(input())
second_number = int(input())
third_number = int(input())

is_first_greatest = (first_number > second_number) and (first_number > third_number)

if is_first_greatest:
    print(first_number)
else:
    is_second_greatest = (second_number > third_number)

    if is_second_greatest:
        print(second_number)
    else:
        print(third_number)
