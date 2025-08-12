number = int(input())
a = 0

if number > 9:
    a = 10
else:
    a = number

for num_1 in range(1, a):
    for num_2 in range(1, a):
        for num_3 in range(1, a):
            for num_4 in range(1, a):
                if num_1 + num_2 == num_3 + num_4 and number % (num_1 + num_2) == 0:
                    print(f"{num_1}{num_2}{num_3}{num_4}", end=" ")