puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

excursion_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

total_toys_count = (
        puzzles +
        talking_dolls +
        teddy_bears +
        minions +
        trucks
)

summ = (
        puzzles * puzzle_price +
        talking_dolls * talking_doll_price +
        teddy_bears * teddy_bear_price +
        minions * minion_price +
        trucks * truck_price
        )

if total_toys_count >= 50:
    summ *= 0.75 #summ = summ - summ * 0.25

summ *= 0.9  # summ = summ - summ * 0.10
remaining_money = summ - excursion_price
money_needed = excursion_price - summ

if summ >= excursion_price:
    print(f"Yes! {remaining_money:.2f} lv left.")
else:
    print(f"Not enough money! {money_needed:.2f} lv needed.")