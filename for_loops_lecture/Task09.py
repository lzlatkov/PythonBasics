user_input = int(input())
left_sum = 0
right_sum = 0

for i in range(user_input):
    number = int(input())
    left_sum += number

for i in range(user_input):
    number = int(input())
    right_sum += number

difference = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {difference}")