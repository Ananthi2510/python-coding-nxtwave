#Reads a number N and prints the sum of N natural numbers

number = int(input())

counter = 0
sum_of_numbers = 0
while counter < number:
    counter = counter + 1
    sum_of_numbers = sum_of_numbers + counter

print(sum_of_numbers)
