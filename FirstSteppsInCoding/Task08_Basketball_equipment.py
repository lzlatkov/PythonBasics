annual_tax = int(input())

basketball_shoes = annual_tax - annual_tax * 0.4
basketball_clothes = basketball_shoes - basketball_shoes * 0.2
basketball_ball = basketball_clothes * 0.25
basketball_accessories = basketball_ball * 0.2

total_cost = annual_tax + basketball_shoes + basketball_clothes + basketball_ball + basketball_accessories

print(total_cost)