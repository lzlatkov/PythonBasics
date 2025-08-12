hour = int(input())
day_of_week = input()

result = "Closed"
if 10 <= hour <= 18 and day_of_week == "Monday":
    result = "open"
elif 10 <= hour <= 18 and day_of_week == "Tuesday":
    result = "open"
elif 10 <= hour <= 18 and day_of_week == "Wednesday":
    result = "open"
elif 10 <= hour <= 18 and day_of_week == "Thursday":
    result = "open"
elif 10 <= hour <= 18 and day_of_week == "Friday":
    result = "open"
elif 10 <= hour <= 18 and day_of_week == "Saturday":
    result = "open"
else:
    result = "closed"


print(result)
