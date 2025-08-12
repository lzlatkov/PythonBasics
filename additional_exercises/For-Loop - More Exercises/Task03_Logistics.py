MICROBUS_PRICE_PER_TON = 200
TRUCK_PRICE_PER_TON = 175
TRAIN_PRICE_PER_TON = 120

# read user input
cargo_count = int(input())
average_cost_per_ton = 0
total_tons = 0
microbus_tons = 0
truck_tons = 0
train_tons = 0

microbus_price = 0
truck_price = 0
train_price = 0

# logic
for num in range (1, cargo_count + 1):
    each_cargo_tons = int(input())
    total_tons += each_cargo_tons
    if each_cargo_tons <= 3:
        microbus_tons += each_cargo_tons
        microbus_price += MICROBUS_PRICE_PER_TON * each_cargo_tons
    elif 4 <= each_cargo_tons <= 11:
        truck_tons += each_cargo_tons
        truck_price += TRUCK_PRICE_PER_TON * each_cargo_tons
    elif each_cargo_tons > 11:
        train_tons += each_cargo_tons
        train_price += TRAIN_PRICE_PER_TON * each_cargo_tons

average_cost_per_ton = (microbus_price + truck_price + train_price) / total_tons

# print output
print(f"{average_cost_per_ton:.2f}")
print(f"{(microbus_tons / total_tons) * 100:.2f}%")
print(f"{(truck_tons / total_tons) * 100:.2f}%")
print(f"{(train_tons / total_tons) * 100:.2f}%")