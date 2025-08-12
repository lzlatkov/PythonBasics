user_input = input()
temp_char = ""
result = 0

for char in range(0, len(user_input)):
    temp_char = user_input[char]
    if temp_char == "a":
        result += 1
    elif temp_char == "e":
        result += 2
    elif temp_char == "i":
        result += 3
    elif temp_char == "o":
        result += 4
    elif temp_char == "u":
        result += 5

print(result)
