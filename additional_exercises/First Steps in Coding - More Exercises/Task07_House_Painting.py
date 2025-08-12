GREEN_PAINT_CONSUMPTION_PER_LITER = 3.4
RED_PAINT_CONSUMPTION_PER_LITER = 4.3

#Read user input
house_height = float(input())
house_length = float(input())
roof_height = float(input())


#Logic
door_space = 1.2 * 2
windows_space = 2 * 1.5 * 1.5

house_total_area = (2 * house_height * house_height - door_space) + (2 * house_length * house_height - windows_space)
roof_total_area = (2 * (house_height * roof_height / 2)) + (2 * house_length * house_height)

total_green_paint = house_total_area / GREEN_PAINT_CONSUMPTION_PER_LITER
total_red_paint = roof_total_area / RED_PAINT_CONSUMPTION_PER_LITER

#Print output
print(f"{total_green_paint:.2f}")
print(f"{total_red_paint:.2f}")