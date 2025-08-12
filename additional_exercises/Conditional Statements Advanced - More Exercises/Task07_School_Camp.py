# read user input
season = input()
group_type = input()
students_count = int(input())
sleep_count = int(input())
sport = ""
sleep_price = 0
total_sleep_price = 0
# logic
if season == "Winter":
    if group_type == "girls" or group_type == "boys":
        sleep_price = 9.6
    if group_type == "mixed":
        sleep_price = 10

    if group_type == "girls":
        sport = "Gymnastics"
    elif group_type == "boys":
        sport = "Judo"
    elif group_type == "mixed":
        sport = "Ski"
elif season == "Spring":
    if group_type == "girls" or group_type == "boys":
        sleep_price = 7.2
    if group_type == "mixed":
        sleep_price = 9.5

    if group_type == "girls":
        sport = "Athletics"
    elif group_type == "boys":
        sport = "Tennis"
    elif group_type == "mixed":
        sport = "Cycling"
elif season == "Summer":
    if group_type == "girls" or group_type == "boys":
        sleep_price = 15
    if group_type == "mixed":
        sleep_price = 20

    if group_type == "girls":
        sport = "Volleyball"
    elif group_type == "boys":
        sport = "Football"
    elif group_type == "mixed":
        sport = "Swimming"

total_sleep_price = sleep_price * sleep_count * students_count

if 10 <= students_count < 20:
    total_sleep_price = total_sleep_price - total_sleep_price * 0.05
elif 20 <= students_count < 50:
    total_sleep_price = total_sleep_price - total_sleep_price * 0.15
elif students_count > 50:
    total_sleep_price = total_sleep_price - total_sleep_price * 0.5
# print output
print(f"{sport} {total_sleep_price:.2f} lv.")
