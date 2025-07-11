#Reads a number N and prints the average of N numbers from 1

number = int(input())

sum_of_numbers = 0
counter = 0

while counter < number:
    counter = counter + 1
    sum_of_numbers = sum_of_numbers + counter

average = sum_of_numbers / number
print(average)
