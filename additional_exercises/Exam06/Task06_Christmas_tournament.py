# Read user input
tournament_days = int(input())
total_won_money = 0
win_counter = 0
lose_counter = 0

# Logic
for i in range(1, tournament_days + 1):
    daily_win_counter = 0
    daily_lose_counter = 0
    bonus_day_money = 0
    daily_won_money = 0
    money_each_day = 0
    while True:
        sport = input()
        if sport == "Finish":
            if daily_win_counter > daily_lose_counter:
                bonus_day_money = money_each_day * 0.1
                daily_won_money = money_each_day + bonus_day_money
            else:
                daily_won_money += money_each_day
            break
        result = input()
        if result == "win":
            money_each_day += 20
            win_counter += 1
            daily_win_counter += 1
        else:
            lose_counter += 1
            daily_lose_counter += 1

    total_won_money += daily_won_money
if win_counter < lose_counter:
    print(f"You lost the tournament! Total raised money: {total_won_money:.2f}")
else:
    total_won_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_won_money:.2f}")