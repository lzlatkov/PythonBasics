number = int(input())
temp_sum = 0
counter = 0
is_true = False

for i in range(number + 1):
    for j in range(number + 1):
        for k in range(number + 1):
            temp_sum = i + j + k
            if i + j + k == number:
                counter += 1

print(counter)