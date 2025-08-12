animal = (input())

result = "unknown"

if animal == "dog":
    result = "mammal"
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    result = "reptile"

print(result)