word = input()

#first three characters
first_part = word[:3]

#remaining characters after the fourth character
second_part = word[4:]

#new string after skipping fourth character
result = first_part + second_part
print(result)
