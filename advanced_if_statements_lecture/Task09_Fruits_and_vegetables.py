name = input()
result = ""

if name == "banana" or name == "apple" or name == "kiwi" or name == "cherry" or name == "lemon" or name == "grapes":
    result = "fruit"
elif name == "tomato" or name == "cucumber" or name == "pepper" or name == "carrot":
    result = "vegetable"
else:
    result = "unknown"

print(result)