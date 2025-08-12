from math import floor, ceil

days_of_absence = int(input())
food_left = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) * 0.001
total_food_needed = 0

#Logic
total_food_needed = dog_food * days_of_absence + cat_food * days_of_absence + turtle_food * days_of_absence

if food_left >= total_food_needed:
    print(f"{floor(food_left - total_food_needed)} kilos of food left.")
else:
    print(f"{ceil(total_food_needed - food_left)} more kilos of food are needed.")