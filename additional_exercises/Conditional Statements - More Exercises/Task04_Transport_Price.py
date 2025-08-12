#Read user input
kilometers = int(input())
time_of_travel = input()
price = 0

# Logic

if kilometers < 20:
    if time_of_travel == "day":
        price = 0.7 + 0.79 * kilometers
    elif time_of_travel == "night":
        price = 0.7 + 0.9 * kilometers
elif kilometers < 100:
    price = 0.09 * kilometers
else:
    price = 0.06 * kilometers

#Print output
print(f"{price:.2f}")