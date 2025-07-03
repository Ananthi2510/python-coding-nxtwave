#reads a string . The string  contains a number except the last character. The last character of the string contains T or H or K.
#Print the Value by multiplying the number in String  with 10 or 100 or 1000 based on the last character.

string = input()

string_length = len(string)
last_index = string_length - 1

number = string[:last_index]
number = int(number)

last_character = string[last_index]

if last_character == "T":
    value = number * 10
elif last_character == "H":
    value = number * 100
elif last_character == "K":
    value = number * 1000

print(value)
