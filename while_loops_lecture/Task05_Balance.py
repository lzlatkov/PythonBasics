balance = 0

while True:
    deposit = input()
    if deposit == "NoMoreMoney":
        break
    deposit = float(deposit)

    if deposit < 0:
        print(f"Invalid operation!")
        break
    print(f"Increase: {deposit:.2f}")
    balance += deposit
print(f"Total: {balance:.2f}")
