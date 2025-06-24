# reads a number  and checks if the triple of the number is divisible by 6

number = int(input())

triple = number * 3

is_triple_divisible = (triple % 6 == 0)

if is_triple_divisible:
    print(triple)
else:
    print(number)
