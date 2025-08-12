number_one = int(input())
number_two = int(input())
number_three = int(input())

for i in range(2, number_one + 1, 2):
    for j in range(2, number_two + 1):
        prime = True
        # for num in range(2, j):
        if number_two % j == 0:
            prime = False
            break
        if not prime:
            continue

        for k in range(2, number_three + 1, 2):

            print(i, j, k)
