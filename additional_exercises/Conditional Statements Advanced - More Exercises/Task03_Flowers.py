BOUQUET_ASSEMBLY_PRICE = 2

# read user inpout
chrysanthemum_count = int(input())
roses_count = int(input())
tulips_count = int(input())
total_flowers_price = 0
season = input()
holiday = input()
total_bouquet_price = 0

# Logic
total_flowers_count = chrysanthemum_count + roses_count + tulips_count

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    roses_price = 4.1
    tulips_price = 2.5
    if holiday == "Y":
        chrysanthemum_price = chrysanthemum_price + chrysanthemum_price * 0.15
        roses_price = roses_price + roses_price * 0.15
        tulips_price = tulips_price + tulips_price * 0.15
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15
    if holiday == "Y":
        chrysanthemum_price = chrysanthemum_price + chrysanthemum_price * 0.15
        roses_price = roses_price + roses_price * 0.15
        tulips_price = tulips_price + tulips_price * 0.15

total_flowers_price = roses_count * roses_price + chrysanthemum_count * chrysanthemum_price + tulips_count * tulips_price

if tulips_count > 7 and season == "Spring":
    total_flowers_price = total_flowers_price - total_flowers_price * 0.05

if roses_count >= 10 and season == "Winter":
    total_flowers_price = total_flowers_price - total_flowers_price * 0.1

if total_flowers_count > 20:
    total_flowers_price = total_flowers_price - total_flowers_price * 0.2

total_bouquet_price = total_flowers_price + BOUQUET_ASSEMBLY_PRICE

# print output
print(f"{total_bouquet_price:.2f}")
