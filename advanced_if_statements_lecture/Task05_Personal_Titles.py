age = float(input())
sex = (input())
result = ""

if age >= 16 and sex == "m":
    result = "Mr."
elif age < 16 and sex == "m":
    result = "Master"
elif age >= 16 and sex == "f":
    result = "Ms."
elif age < 16 and sex == "f":
    result = "Miss"

print(result)