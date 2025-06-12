#Reads two words
first_word = input()
second_word = input()

first_word_length = len(first_word)
second_word_length = len(second_word)

#Check if the second word is the last part of the first word 
start_index = first_word_length - second_word_length
part = first_word[start_index: ]

result = part == second_word
print(result)
