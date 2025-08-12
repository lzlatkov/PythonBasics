user_input = int(input())
sum = 0

while True:
    number = int(input())
    sum += number
    if sum >= user_input:
        break

print(sum)