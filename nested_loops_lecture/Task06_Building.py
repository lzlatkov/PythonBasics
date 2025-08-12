floors = int(input())
apartments = int(input())

for floor in range(floors, 0, -1):
    for apartment in range(apartments):
        if floor == floors:
            print(f"L{floor}{apartment}", end=" ")
        elif floor % 2 == 0:
            print(f"O{floor}{apartment}", end=" ")
        else:
            print(f"A{floor}{apartment}", end=" ")
    print()
