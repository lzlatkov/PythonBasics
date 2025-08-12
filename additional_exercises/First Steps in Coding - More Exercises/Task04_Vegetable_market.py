vegetable_price_per_kilo = float(input())
fruit_price_per_kilo = float(input())
total_vegetables_kg = float(input())
total_fruits_kg = float(input())

total_profit = vegetable_price_per_kilo * total_vegetables_kg + fruit_price_per_kilo * total_fruits_kg
total_profit_euro = total_profit / 1.94

print(f"{total_profit:.2f}")
