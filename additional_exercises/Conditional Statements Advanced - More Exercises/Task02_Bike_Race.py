# Read User Input
junior_contestants_count = int(input())
senior_contestants_count = int(input())
race_type = input()
participation_tax_juniors = 0
participation_tax_seniors = 0
total_sum = 0
expenses = 0
money_donated = 0

# Logic
if race_type == "trail":
    participation_tax_juniors = 5.5
    participation_tax_seniors = 7
elif race_type == "cross-country":
    participation_tax_juniors = 8
    participation_tax_seniors = 9.5
    if junior_contestants_count + senior_contestants_count >= 50:
        participation_tax_juniors = participation_tax_juniors - participation_tax_juniors * 0.25
        participation_tax_seniors = participation_tax_seniors - participation_tax_seniors * 0.25
elif race_type == "downhill":
    participation_tax_juniors = 12.25
    participation_tax_seniors = 13.75
elif race_type == "road":
    participation_tax_juniors = 20
    participation_tax_seniors = 21.5

total_sum = participation_tax_juniors * junior_contestants_count + participation_tax_seniors * senior_contestants_count
expenses = total_sum * 0.05

money_donated = total_sum - expenses

# print output
print(f"{money_donated:.2f}")