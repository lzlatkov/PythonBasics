from math import floor

tournament_count = int(input())
starting_points = int(input())

points_bonus = 0
tournaments_win = 0

for i in range(tournament_count):
    result = input()
    if result == "W":
        points_bonus += 2000
        tournaments_win += 1
    elif result == "F":
        points_bonus += 1200
    elif result == "SF":
        points_bonus += 720


print(f"Final points: {starting_points + points_bonus}")
print(f'Average points: {floor(points_bonus / tournament_count)}')
print(f"{(tournaments_win /tournament_count) * 100:.2f}%")
