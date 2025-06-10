#get an word
word = input()

#get a number
number = int(input())

length = len(word)

#the last three characters of the word should be printed given number of times
result = word[length-3 : ] * number
print(result)
