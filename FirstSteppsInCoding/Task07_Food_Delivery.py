chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15

chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())

total_menu_cost = chicken_menu * chicken_menu_count + fish_menu * fish_menu_count + vegetarian_menu_count * vegetarian_menu
desert = total_menu_cost * 0.20
delivery_price = 2.5
order_price = total_menu_cost + desert + delivery_price

print(order_price)