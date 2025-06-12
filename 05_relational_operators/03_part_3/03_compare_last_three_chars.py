#Reads two strings
first_word = input()
second_word = input()

#find the length of the words
first_word_length = len(first_word)
second_word_length = len(second_word)

#Check if the last three characters in the given two words are same
result = first_word[first_word_length-3: ] == second_word[second_word_length-3: ]
