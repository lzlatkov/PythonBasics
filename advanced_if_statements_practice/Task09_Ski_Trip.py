days = int(input())
place = input()
rating = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35

nights = days - 1

if nights < 10:
    if place == "room for one person":
        price = nights * room_for_one_person
    elif place == "apartment":
        price = (nights * apartment) - (nights * apartment) * 0.3
    elif place == "president apartment":
        price = (nights * president_apartment) - (nights * president_apartment) * 0.1
elif nights > 15:
    if place == "room for one person":
        price = nights * room_for_one_person
    elif place == "apartment":
        price = (nights * apartment) - (nights * apartment) * 0.5
    elif place == "president apartment":
        price = (nights * president_apartment) - (nights * president_apartment) * 0.2
else:
    if place == "room for one person":
        price = nights * room_for_one_person
    elif place == "apartment":
        price = (nights * apartment) - (nights * apartment) * 0.35
    elif place == "president apartment":
        price = (nights * president_apartment) - (nights * president_apartment) * 0.15

if rating == "positive":
    price *= 1.25
elif rating == "negative":
    price *= 0.9

print(f"{price:.2f}")
