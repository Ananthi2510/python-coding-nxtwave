word = input()
no_of_characters = input()
no_of_characters = int(no_of_characters)

word_length = len(word)
start_index = word_length - no_of_characters

part = word[start_index:]
print(part)
