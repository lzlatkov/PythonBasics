# Read User input
minutes = int(input())
daily_walks = int(input())
calories_eaten = int(input())
calories_burn = 5
goal = 0

#Logic
total_minutes = minutes * daily_walks
total_calories_burned = total_minutes * calories_burn
goal = calories_eaten * 0.5


if total_calories_burned >= goal:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories_burned}.")
