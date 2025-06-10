word = input()

length = len(word)
no_of_stars = length - 4

first_two_chars = word[ :2]
last_two_chars = word[length - 2: ]

result = first_two_chars + ("*" * no_of_stars) + last_two_chars
print(result)
