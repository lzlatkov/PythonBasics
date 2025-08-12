nylon_price_per_square_meter = 1.50
paint_price_per_liter = 14.50
thinner_price_per_liter = 5.00
bags_price = 0.40

nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon += 2
paint += paint * 0.10

nylon_price = nylon_price_per_square_meter * nylon
paint_price = paint_price_per_liter * paint
thinner_price = thinner_price_per_liter * thinner
total_expenses_matherials = nylon_price + paint_price + thinner_price + bags_price
price_laber_per_hour = total_expenses_matherials * 0.30
total_cost = total_expenses_matherials + hours * price_laber_per_hour

print(total_cost)
