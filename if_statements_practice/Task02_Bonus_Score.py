starting_number = int(input())

bonus_points = 0
extra_bonus_points = 0

if starting_number <= 100:
    bonus_points = 5
elif starting_number > 1000:
    bonus_points = starting_number * 0.1
else:
    bonus_points = starting_number * 0.2

if starting_number % 2 == 0:
    extra_bonus_points = 1
elif starting_number % 10 == 5:
    extra_bonus_points = 2

total_bonus_points = bonus_points + extra_bonus_points

print(total_bonus_points)
print(starting_number + total_bonus_points)