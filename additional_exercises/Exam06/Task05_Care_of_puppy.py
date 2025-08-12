total_food_bought = int(input()) * 1000
total_food_eaten = 0

while True:
    food_eaten = input()
    if food_eaten == "Adopted":
        break
    total_food_eaten += int(food_eaten)

if total_food_eaten <= total_food_bought:
    print(f"Food is enough! Leftovers: {total_food_bought - total_food_eaten} grams.")
else:
    print(f"Food is not enough. You need {total_food_eaten - total_food_bought} grams more.")
