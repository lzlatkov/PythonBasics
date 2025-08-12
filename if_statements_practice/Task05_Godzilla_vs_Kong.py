budget = float(input())
statists = int(input())
clothing = float(input())

decor = budget * 0.10

if statists > 150:
    clothing = clothing - clothing * 0.10

expenses_statists = statists * clothing
total_expenses = expenses_statists + decor

if total_expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_expenses - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_expenses:.2f} leva left.")