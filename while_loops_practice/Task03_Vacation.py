vacation_money = float(input())
available_money = float(input())
days_counter = 0
spending_counter = 0
action = ""

while available_money < vacation_money and spending_counter < 5:
    action = input()
    money = float(input())
    days_counter += 1
    if action == "spend":
        spending_counter += 1
        available_money -= money
        if available_money < 0:
            available_money = 0
    elif action == "save":
        spending_counter = 0
        available_money += money
if spending_counter >= 5:
    print(f"You can't save the money.")
    print(days_counter)
if available_money >= vacation_money:
    print(f"You saved the money for {days_counter} days.")
