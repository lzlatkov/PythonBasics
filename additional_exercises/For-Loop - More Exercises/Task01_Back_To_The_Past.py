CURRENT_YEARS = 18

# read user input
inherited_money = float(input())
year = int(input())
money_spend = 0
counter = 0
# logic
for num in range (1800, year + 1):

    if num % 2 == 0:
        money_spend += 12000
    else:
        money_spend += 12000 + 50 * (CURRENT_YEARS + counter)
    counter += 1
money_left = inherited_money - money_spend
# print output
if money_spend <= inherited_money:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left." )
else:
    print(f"He will need {abs(money_left):.2f} dollars to survive.")