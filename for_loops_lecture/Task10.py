user_input = int(input())

even_numbers = 0
odd_numbers = 0


for i in range(user_input):
    number = int(input())
    if i % 2 == 0:
        even_numbers += number
    else:
        odd_numbers += number

if even_numbers == odd_numbers:
    print("Yes")
    print(f"Sum = {even_numbers}")
else:
    print("No")
    print(f"Diff = {abs(even_numbers - odd_numbers)}")

