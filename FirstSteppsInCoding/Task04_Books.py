total_pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_hours_to_read = total_pages // pages_per_hour
total_hours = total_hours_to_read // days

print(total_hours)
