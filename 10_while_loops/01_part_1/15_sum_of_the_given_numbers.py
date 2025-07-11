#reads N inputs and prints the sum of the given input integers.
N = int(input())

counter = 0
sum = 0
while counter < N:
    number = int(input())
    sum = (sum + number)
    counter = (counter + 1)

print(sum)

