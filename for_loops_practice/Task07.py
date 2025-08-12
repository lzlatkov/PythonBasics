groups_count = int(input())
destination = ""
total_people = 0
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(groups_count):
    people = int(input())

    if people < 6:
        musala += people
    elif 6 <= people <= 12:
        monblan += people
    elif 13 <= people <= 25:
        kilimanjaro += people
    elif 26 <= people <= 40:
        k2 += people
    else:
        destination = "Everest"
        everest += people

total_people = musala + monblan + k2 + kilimanjaro + everest

print(f"{musala / total_people * 100:.2f}%")
print(f"{monblan / total_people * 100:.2f}%")
print(f"{kilimanjaro / total_people * 100:.2f}%")
print(f"{k2 / total_people * 100:.2f}%")
print(f"{everest / total_people * 100:.2f}%")