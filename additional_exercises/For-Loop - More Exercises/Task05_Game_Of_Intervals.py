# read user input
total_game_stages = int(input())
total_game_points = 0
range_one_counter = 0
range_two_counter = 0
range_three_counter = 0
range_four_counter = 0
range_five_counter = 0
invalid_counter = 0
# logic
for _ in range (1, total_game_stages + 1):
    number = int(input())
    if 0 <= number <= 9:
        range_one_counter += 1
        total_game_points += number * 0.2
    elif 10 <= number <= 19:
        range_two_counter += 1
        total_game_points += number * 0.3
    elif 20 <= number <= 29:
        range_three_counter += 1
        total_game_points += number * 0.4
    elif 30 <= number <= 39:
        range_four_counter += 1
        total_game_points += 50
    elif 40 <= number <= 50:
        range_five_counter += 1
        total_game_points += 100
    else:
        invalid_counter += 1
        total_game_points = total_game_points / 2

# print output
print(f"{total_game_points:.2f}")
print(f"From 0 to 9: {(range_one_counter / total_game_stages) * 100:.2f}%")
print(f"From 10 to 19: {(range_two_counter / total_game_stages) * 100:.2f}%")
print(f"From 20 to 29: {(range_three_counter / total_game_stages) * 100:.2f}%")
print(f"From 30 to 39: {(range_four_counter / total_game_stages) * 100:.2f}%")
print(f"From 40 to 50: {(range_five_counter / total_game_stages) * 100:.2f}%")
print(f"Invalid numbers: {(invalid_counter / total_game_stages) * 100:.2f}%")
