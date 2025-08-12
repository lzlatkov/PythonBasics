
while True:
    user_input = float(input())
    result = user_input * 2
    if user_input < 0:
        print(f"Negative number!")
        break
    print(f"Result: {result:.2f}")