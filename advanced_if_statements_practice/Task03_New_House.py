type_of_flowers = input()
flowers_count = int(input())
budget = int(input())

roses_price = 5
dahlia_price = 3.8
tulip_price = 2.8
narcissus_price = 3
gladiolus_price = 2.5

price = 0

if type_of_flowers == "Roses":
    price = roses_price * flowers_count

    if flowers_count > 80:
        price = price - price * 0.1

elif type_of_flowers == "Dahlias":
    price = dahlia_price * flowers_count

    if flowers_count > 90:
        price = price - price * 0.15

elif type_of_flowers == "Tulips":
    price = tulip_price * flowers_count

    if flowers_count > 80:
        price = price - price * 0.15

elif type_of_flowers == "Narcissus":
    price = narcissus_price * flowers_count

    if flowers_count < 120:
        price = price + price * 0.15

elif type_of_flowers == "Gladiolus":
    price = gladiolus_price * flowers_count

    if flowers_count < 80:
        price = price + price * 0.2

if budget >= price:
    print(f"Hey, you have a great garden with {flowers_count} {type_of_flowers} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")