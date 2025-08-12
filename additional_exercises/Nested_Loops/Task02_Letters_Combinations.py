
first_letter = input()
second_letter = input()
third_letter = input()
counter = 0

for i in range(ord(first_letter), ord(second_letter) + 1):
    if i == ord(third_letter):
        continue
    for j in range(ord(first_letter), ord(second_letter) + 1):
        if j == ord(third_letter):
            continue
        for k in range(ord(first_letter), ord(second_letter) + 1):
            if k == ord(third_letter):
                continue
            counter += 1
            print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")

print(counter)