#Read User Input
from math import floor, ceil

MAGNOLIA_PRICE = 3.25
HYACINTH_PRICE = 4  #Зюмбюл
ROSES_PRICE = 3.5
CACTUS_PRICE = 8
tax = 0.05
profit = 0
total_sales = 0

magnolia_count = int(input())
hyacinth_count = int(input())
roses_count = int(input())
cactus_count = int(input())
present_price = float(input())

#Logic
total_sales = magnolia_count * MAGNOLIA_PRICE + hyacinth_count * HYACINTH_PRICE + roses_count * ROSES_PRICE + cactus_count * CACTUS_PRICE
tax = total_sales * tax

profit = total_sales - tax

if profit >= present_price:
    print(f"She is left with {floor(profit - present_price)} leva.")
else:
    print(f"She will have to borrow {ceil(present_price - profit)} leva.")