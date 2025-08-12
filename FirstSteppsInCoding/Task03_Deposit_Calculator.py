deposited_summ = float(input())
deposit_period = int(input())
interest_rate = float(input()) / 100

total_summ = deposited_summ + deposit_period * ((deposited_summ * interest_rate) / 12)

print(total_summ)