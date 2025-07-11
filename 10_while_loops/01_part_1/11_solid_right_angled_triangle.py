#print the right-angled triangular pattern of N lines using an asterisk(*) character.

number = int(input())

counter = 1
while counter <= number:
    print("* " * counter)
    counter = (counter + 1)
