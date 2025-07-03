#reads an operator  and two numbers.
Print the result by doing arithmetic operations on the two numbers based on the operator

operator = input()
first_number = int(input())
second_number = int(input())

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    print(first_number / second_number)
else:
    print(first_number % second_number)
