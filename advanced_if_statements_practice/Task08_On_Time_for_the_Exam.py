exam_hour = int(input())
exam_minutes = int(input())
attendance_hour = int(input())
attendance_minutes = int(input())

total_exam_minutes = exam_hour * 60 + exam_minutes
total_attendance_minutes = attendance_hour * 60 + attendance_minutes

if 30 > total_exam_minutes - total_attendance_minutes >= 0:
    print("On time")
elif total_exam_minutes - total_attendance_minutes < 0:
    print("Late")
elif total_exam_minutes - total_attendance_minutes > 30:
    print("Early")

hours = abs(total_exam_minutes - total_attendance_minutes) // 60
minutes = abs(total_exam_minutes - total_attendance_minutes) % 60
output = ""
if hours > 0:
    output += f"{hours}{minutes:02d}hours before the start"
elif minutes > 0:
    output += f"{minutes} minutes after the start"

print(output)