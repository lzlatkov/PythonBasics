degrees = int(input())
day_of_time = input()

result = ""

if day_of_time == "Morning":
    if 10<= degrees <= 18:
        result = f"It's {degrees} degrees, get your Sweatshirt and Sneakers."
    elif 18 < degrees <= 24:
        result = f"It's {degrees} degrees, get your Shirt and Moccasins."
    elif  degrees >= 25:
        result = f"It's {degrees} degrees, get your T-Shirt and Sandals."
elif day_of_time == "Afternoon":
    if 10<= degrees <= 18:
        result = f"It's {degrees} degrees, get your Shirt and Moccasins."
    elif 18 < degrees <= 24:
        result = f"It's {degrees} degrees, get your T-Shirt and Sandals."
    elif  degrees >= 25:
        result = f"It's {degrees} degrees, get your Swim Suit and Barefoot."
else:
    if 10<= degrees <= 18:
        result = f"It's {degrees} degrees, get your Shirt and Moccasins."
    elif 18 < degrees <= 24:
        result = f"It's {degrees} degrees, get your Shirt and Moccasins."
    elif  degrees >= 25:
        result = f"It's {degrees} degrees, get your Shirt and Moccasins."

print(result)