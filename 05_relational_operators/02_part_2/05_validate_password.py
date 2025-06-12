#Reads a string
password = input()
length = len(password)

#check the password is valid(length greater than 7)
is_valid_password = length > 7
print(is_valid_password)
