# reads a string and prints each character of the given string on a new line.

string = input()

index = 0
length = len(string)

while index < length:
    character = string[index]
    print(character)
    index = index + 1
