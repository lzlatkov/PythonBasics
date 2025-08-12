resistance_seconds = 12.5
resistance_meters = 15


record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_meter = float(input())

water_resistance_time = distance_in_meters // resistance_meters * resistance_seconds

time = distance_in_meters * time_in_seconds_per_meter + water_resistance_time

if time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {time - record_in_seconds:.2f} seconds slower.")
