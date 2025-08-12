years = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_as_a_gift = 10
money_profit = 0
toys_sold_profit = 0
brother_tax = 1
yearly_money_increase = 10

for age in range(1, years + 1):
    if age % 2 == 0:
        money_profit += money_as_a_gift - brother_tax
        money_as_a_gift += yearly_money_increase
    else:
        toys_sold_profit += toy_price

total_money_collected = money_profit + toys_sold_profit

if total_money_collected >= washing_machine_price:
    print(f"Yes! {total_money_collected - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - total_money_collected:.2f}")



