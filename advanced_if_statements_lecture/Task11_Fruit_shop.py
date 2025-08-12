fruit = input()
day_of_week = input()
qty = float(input())

total_price = "error"

if day_of_week == "Sunday" or day_of_week == "Saturday":
    if fruit == "banana":
        price = 2.7
        total_price = price * qty
    elif fruit == "apple":
        price = 1.25
        total_price = price * qty
    elif fruit == "orange":
        price = 0.90
        total_price = price * qty
    elif fruit == "grapefruit":
        price = 1.6
        total_price = price * qty
    elif fruit == "kiwi":
        price = 3
        total_price = price * qty
    elif fruit == "pineapple":
        price = 5.6
        total_price = price * qty
    elif fruit == "grapes":
        price = 4.2
        total_price = price * qty
elif day_of_week == "Monday" \
        or day_of_week == "Tuesday" \
        or day_of_week == "Wednesday" \
        or day_of_week == "Thursday" \
        or day_of_week == "Friday":
    if fruit == "banana":
        price = 2.5
        total_price = price * qty
    elif fruit == "apple":
        price = 1.2
        total_price = price * qty
    elif fruit == "orange":
        price = 0.85
        total_price = price * qty
    elif fruit == "grapefruit":
        price = 1.45
        total_price = price * qty
    elif fruit == "kiwi":
        price = 2.7
        total_price = price * qty
    elif fruit == "pineapple":
        price = 5.5
        total_price = price * qty
    elif fruit == "grapes":
        price = 3.85
        total_price = price * qty
else:
    total_price = "error"

if total_price == "error":
    print(total_price)
else:
    print(f"{total_price:.2f}")