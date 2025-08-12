lenght_in_centimeters = int(input())
width_in_centimeters = int(input())
height_in_centimeters = int(input())
percent_extra_usage = float(input()) / 100

volume = lenght_in_centimeters * width_in_centimeters * height_in_centimeters / 1000

liters = volume * percent_extra_usage
volume = volume - liters

print(volume)




