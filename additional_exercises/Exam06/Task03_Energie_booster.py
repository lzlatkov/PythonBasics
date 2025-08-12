# Read User input
fruit = input()
size = input()
purchased_sets = int(input())
pack_size = 0
price = 0
current_price = 0
# Logic
if size == "small":
    pack_size = 2
    if fruit == "Watermelon":
        price = 56
    elif fruit == "Mango":
        price = 33.66
    elif fruit == "Pineapple":
        price = 42.10
    elif fruit == "Raspberry":
        price = 20
    current_price = pack_size * price
elif size == "big":
    pack_size = 5
    if fruit == "Watermelon":
        price = 28.70
    elif fruit == "Mango":
        price = 19.60
    elif fruit == "Pineapple":
        price = 24.80
    elif fruit == "Raspberry":
        price = 15.20
    current_price = pack_size * price

total_price = current_price * purchased_sets

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.5

print(f"{total_price:.2f} lv.")