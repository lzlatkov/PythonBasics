projection = (input())
rows = int(input())
columns = int(input())


premiere_price = 12
normal_price = 7.5
discount_price = 5

total_seats = rows * columns
profit = 0

if projection == "Premiere":
    profit = total_seats * premiere_price
elif projection == "Normal":
    profit = total_seats * normal_price
elif projection == "Discount":
    profit = total_seats * discount_price

print(f"{profit:.2f} leva")