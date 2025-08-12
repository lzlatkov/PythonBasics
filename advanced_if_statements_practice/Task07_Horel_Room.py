month = input()
sleep_count = int(input())

if month == "May" or month == "October":
    studio = 50
    apartment = 65

    if sleep_count > 14:
        studio *= 0.70
    elif sleep_count > 7:
        studio *= 0.95

elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.7
    if sleep_count > 14:
        studio *= 0.8

elif month == "July" or month == "August":
    studio = 76
    apartment = 77

if sleep_count > 14:
    apartment *= 0.9

print(f"Apartment: {apartment * sleep_count:.2f} lv.")
print(f"Studio: {studio * sleep_count:.2f} lv.")
