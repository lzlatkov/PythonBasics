degrees = float(input())
output = None

if 26.00 <= degrees <= 35.00:
    output = "Hot"
elif 20.1 <= degrees <= 25.9:
    output = "Warm"
elif 15.00 <= degrees <= 20.00:
    output = "Mild"
elif 12.00 <= degrees <= 14.9:
    output = "Cool"
elif 5.00 <= degrees <= 11.9:
    output = "Cold"
else:
    output = "unknown"

print(output)
