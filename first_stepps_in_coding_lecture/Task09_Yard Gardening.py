price_for_square_meter = 7.61
discount_percentage = 0.18

square_meter = float(input())
total_price = price_for_square_meter * square_meter
discount = total_price * discount_percentage
end_price = total_price - discount

print(f'The final price is: {end_price} lv.')
print(f'The discount is : {discount} lv.')
