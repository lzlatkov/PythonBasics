number_one = int(input())
number_two = int(input())
magic_number = int(input())

counter = 0
is_fount = False

for i in range(number_one, number_two + 1):
    if is_fount:
        break
    for j in range(number_one, number_two + 1):
        counter += 1
        if i + j == magic_number:
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            is_fount = True
            break

if not is_fount:
    print(f"{counter} combinations - neither equals {magic_number}")

