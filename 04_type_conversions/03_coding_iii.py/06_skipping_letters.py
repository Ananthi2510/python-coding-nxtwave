word = input()
n = int(input())

before = word[:n]
after = word[n+1:]

#prints the given word without the character at the given index.
result = before + after
print(result)
