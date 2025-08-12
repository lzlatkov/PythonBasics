VIP_TICKET_PRICE = 499.99
NORMAL_TICKET_PRICE = 249.99

#user input
budget = float(input())
category = input()
group_members = int(input())
remaining_money_after_transport = 0
transport_price = 0
money_for_tickets = 0
money_left = 0

# Logic
if group_members < 5:
    transport_price = budget * 0.75
elif 5 <= group_members <= 9:
    transport_price = budget * 0.6
elif 10 <= group_members <= 24:
    transport_price = budget * 0.5
elif 25 <= group_members <= 49:
    transport_price = budget * 0.4
elif group_members >= 50:
    transport_price = budget * 0.25

remaining_money_after_transport = budget - transport_price

if category == "VIP":
    money_for_tickets = group_members * VIP_TICKET_PRICE
elif category == "Normal":
    money_for_tickets = group_members * NORMAL_TICKET_PRICE
money_left = remaining_money_after_transport - money_for_tickets

# Print output
if money_left > 0:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(money_left):.2f} leva.")
