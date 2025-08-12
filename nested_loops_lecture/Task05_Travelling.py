

while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    saved_money = 0
    while True:
        saved_sum = float(input())
        saved_money += saved_sum

        if saved_money >= budget:
            print(f"Going to {destination}!")
            break
