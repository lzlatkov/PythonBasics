number = int(input())
counter = 0

for row in range(1, number + 1):
    if counter == number:
        break
    for column in range(1, row +1):
        counter += 1
        print(counter, end=" ")

        if counter == number:
            break
    print()