#Reads two strings S1 and S2(no. of chars should be same)
S1 = input()
S2 = input()

first_word_length = len(S1)
second_word_length = len(S2)

#Check is S2 is a part of S1
result = S1[0: second_word_length] == S2
print(result)
