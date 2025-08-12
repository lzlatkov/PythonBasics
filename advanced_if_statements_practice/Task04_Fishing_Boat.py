budget = int(input())
season = input()
fishers_count = int(input())

total_price = 0

if season == "Spring":
    total_price = 3000

elif season == "Summer":
    total_price = 4200

elif season == "Autumn":
    total_price = 4200

elif season == "Winter":
    total_price = 2600


if fishers_count <= 6:
    total_price *= 0.9

elif 6 < fishers_count <= 11:
    total_price *= 0.85

elif fishers_count > 11:
    total_price *= 0.75


if fishers_count % 2 == 0 and season != "Autumn":
    total_price *= 0.95

if budget >= total_price:
    print(f"Yes! You have {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva.")