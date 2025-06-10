#to read a srring and prints the second half part of the string
word = input()
length = len(word)
half_length = int((length/2) )
half_word = word[half_length: ]
print(half_word)
