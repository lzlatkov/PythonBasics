CLAMS_PRICE = 7.5

# Read User Input
mackerel_price = float(input())  # скумрия
sprat_price = float(input())     # цаца
bonito_kg = float(input())       # паламуд
safrid_kg = float(input())       # сафрид
clams_kg = int(input())          # миди

# Logic
bonito_price = mackerel_price * 1.6
safrid_price = sprat_price * 1.8

total_price = bonito_price * bonito_kg + safrid_price * safrid_kg + clams_kg * CLAMS_PRICE

#Print Output
print(f"{total_price:.2f}")
