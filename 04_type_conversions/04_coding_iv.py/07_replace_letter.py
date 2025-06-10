#read a word , index and letter
word = input()
index = int(input())
letter = input()

#print the word by replacing the letter at the given index with the given letter
result = word[0:index] + letter + word[index+1: ]
print(result)
