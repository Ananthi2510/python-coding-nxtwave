#reads a word and prints each character of the word in a new line

a = input()

length = len(a)
counter = 0

while counter <= (length - 1):
    print(a[counter])
    counter = (counter + 1)
