#Read user input
days = int(input())
total_food = float(input())
total_food_eaten = 0
biscuits = 0
total_cat_food_eaten = 0
total_dog_food_eaten = 0

#Logic
for i in range(1, days + 1):
    cat_food = int(input())
    dog_food = int(input())
    if i % 3 == 0:
        biscuits += (cat_food + dog_food) * 0.1

    total_food_eaten += (cat_food + dog_food)
    total_cat_food_eaten += cat_food
    total_dog_food_eaten += dog_food

#print output
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_food_eaten / total_food * 100:.2f}% of the food has been eaten.")
print(f"{total_cat_food_eaten / total_food_eaten * 100:.2f}% eaten from the dog.")
print(f"{total_dog_food_eaten / total_food_eaten * 100:.2f}% eaten from the cat.")