#Reads two words and a index
first_string = input()
second_string = input()
start_index = int(input())

second_string_length = len(second_string)

#Check if the second_string starts at the index in first_string
end_index = start_index + second_string_length
part = first_string[start_index:end_index]

result = part == second_string
print(result)
