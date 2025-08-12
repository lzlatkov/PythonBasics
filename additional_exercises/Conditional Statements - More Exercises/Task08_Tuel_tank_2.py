GAS_PRICE = 0.93
GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33

fuel_type = input()
liters = float(input())
club_card = input()
fuel_price = 0
total_price = 0

#Logic
if fuel_type == "Gas":
    if club_card == "Yes":
        GAS_PRICE = GAS_PRICE - 0.08
    elif club_card == "No":
        pass
    if 20 <= liters <= 25:
        discount = liters * GAS_PRICE * 0.08
        fuel_price = liters * GAS_PRICE - discount
    elif liters > 25:
        discount = liters * GAS_PRICE * 0.1
        fuel_price = liters * GAS_PRICE - discount
    else:
        fuel_price = GAS_PRICE * liters
elif fuel_type == "Gasoline":
    if club_card == "Yes":
        GASOLINE_PRICE = GASOLINE_PRICE - 0.18
    elif club_card == "No":
        pass
    if 20 <= liters <= 25:
        discount = liters * GASOLINE_PRICE * 0.08
        fuel_price = liters * GASOLINE_PRICE - discount
    elif liters > 25:
        discount = liters * GASOLINE_PRICE * 0.1
        fuel_price = liters * GASOLINE_PRICE - discount
    else:
        fuel_price = GASOLINE_PRICE * liters
elif fuel_type == "Diesel":
    if club_card == "Yes":
        DIESEL_PRICE = DIESEL_PRICE - 0.12
    elif club_card == "No":
        pass
    if 20 <= liters <= 25:
        discount = liters * DIESEL_PRICE * 0.08
        fuel_price = liters * DIESEL_PRICE - discount
    elif liters > 25:
        discount = liters * DIESEL_PRICE * 0.1
        fuel_price = liters * DIESEL_PRICE - discount
    else:
        fuel_price = DIESEL_PRICE * liters
#Print output
print(f"{fuel_price:.2f} lv.")