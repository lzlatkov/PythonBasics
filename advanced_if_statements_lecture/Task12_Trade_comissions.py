city = input()
sales = float(input())

commission = 0
result = "error"

if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05
        result = sales * commission
    elif 500 < sales <= 1000:
        commission = 0.07
        result = sales * commission
    elif 1000 < sales <= 10000:
        commission = 0.08
        result = sales * commission
    elif sales > 10000:
        commission = 0.12
        result = sales * commission
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045
        result = sales * commission
    elif 500 < sales <= 1000:
        commission = 0.075
        result = sales * commission
    elif 1000 < sales <= 10000:
        commission = 0.1
        result = sales * commission
    elif sales > 10000:
        commission = 0.13
        result = sales * commission
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055
        result = sales * commission
    elif 500 < sales <= 1000:
        commission = 0.08
        result = sales * commission
    elif 1000 < sales <= 10000:
        commission = 0.12
        result = sales * commission
    elif sales > 10000:
        commission = 0.145
        result = sales * commission
else:
    result = "error"

if result == "error":
    print("error")
else:
    print(f"{result:.2f}")