user_input = int(input())

max_num = float("-inf")
sum = 0

for number in range(0, user_input):
    temp_input = int(input())

    if temp_input > max_num:
        max_num = temp_input

    sum += temp_input

differance = sum - max_num

if max_num == differance:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - differance)}")



