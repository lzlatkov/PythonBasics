from math import floor, ceil

ONE_LITER_PRODUCTION = 2.5

square_meters = int(input())
grapes_per_square_meter = float(input())
needed_liters_wine = int(input())
workers = int(input())

wine_square_meters = square_meters * 0.4
total_wine_liters = (wine_square_meters * grapes_per_square_meter) / ONE_LITER_PRODUCTION

if total_wine_liters < needed_liters_wine:
    print(f"It will be a tough winter! More {floor(needed_liters_wine - total_wine_liters)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(total_wine_liters)} liters.")
    print(f"{ceil(total_wine_liters - needed_liters_wine)} liters left -> {ceil((total_wine_liters - needed_liters_wine) / workers)} liters "
          f"per person.")

