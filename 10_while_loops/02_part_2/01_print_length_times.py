#reads a string and prints the first character of the given string on N lines, where N is the length of the given string.

string = input()

counter = 0
length = len(string)
first_character = string[0]

while counter < length:
    print(first_character)
    counter = counter + 1
