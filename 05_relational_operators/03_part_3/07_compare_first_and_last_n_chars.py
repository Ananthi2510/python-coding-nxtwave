#Reads a word and a number N
word = input()
N = int(input())

length = len(word)

#Checks if the first N characters of the string and the last N characters of the string are, not the same
result = word[0:N] != word[length-N:]
print(result)
