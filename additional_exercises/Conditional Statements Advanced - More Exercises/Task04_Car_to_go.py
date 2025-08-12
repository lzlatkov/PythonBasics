# read user input
budget = float(input())
season = input()
car_price = 0

# logic
if budget <= 100:
    class_type = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = budget * 0.35
    elif season == "Winter":
        car_type = "Jeep"
        car_price = budget * 0.65
elif 100 < budget <= 500:
    class_type = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = budget * 0.45
    elif season == "Winter":
        car_type = "Jeep"
        car_price = budget * 0.8
else:
    class_type = "Luxury class"
    car_type = "Jeep"
    car_price = budget * 0.9

# print output
print(class_type)
print(f"{car_type} - {car_price:.2f}")