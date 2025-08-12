hours = int(input())
minutes = int(input()) + 15

# bonus_minutes = 15

# minutes += bonus_minutes

if minutes > 59:
    hours += 1
    minutes -= 60

if hours > 23:
    hours -= 24

print(f"{hours}:{minutes:02d}")