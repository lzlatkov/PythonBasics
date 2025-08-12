pen_pack_price = 5.80
marker_pack_price = 7.20
detergent_price = 1.20

pen_packs = int(input())
marker_packs = int(input())
detergent_in_liters = int(input())
discount = int(input()) / 100

total_summ_before_discount = pen_packs * pen_pack_price + marker_packs * marker_pack_price + detergent_price * detergent_in_liters
discount_summ = total_summ_before_discount * discount
total_summ = total_summ_before_discount - discount_summ

print(total_summ)




