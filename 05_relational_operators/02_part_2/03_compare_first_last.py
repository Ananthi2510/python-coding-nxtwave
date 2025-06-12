#Reads a word
word = input()

length = len(word)

first_letter = word[0]
last_letter = word[length - 1]

#check if first and last letters are not same
result = first_letter != last_letter

print(result)
