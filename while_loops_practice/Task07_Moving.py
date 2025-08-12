apartment_width = int(input())
apartment_length = int(input())
apartment_height = int(input())

apartment_space = apartment_height * apartment_length * apartment_width
boxes_space = 0

while apartment_space >= boxes_space:
    boxes = input()
    if boxes == "Done":
        break

    boxes = int(boxes)
    boxes_space += boxes

if apartment_space >= boxes_space:
    print(f"{apartment_space - boxes_space} Cubic meters left.")
else:
    print(f"No more free space! You need {boxes_space - apartment_space} Cubic meters more.")