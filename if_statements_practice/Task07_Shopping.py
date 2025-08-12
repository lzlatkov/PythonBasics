budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_card_price = 250

video_cards_price = video_card_price * video_cards
processors_price = processors * video_cards_price * 0.35
ram_memory_price = ram_memory * video_cards_price * 0.10

total_price = video_cards_price + processors_price + ram_memory_price

if video_cards > processors:
    total_price = total_price - total_price * 0.15

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")