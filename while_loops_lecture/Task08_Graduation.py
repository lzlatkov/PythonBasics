name = input()

failed_grades = 0
average_grade = 0
current_class = 1

while True:
    grade = float(input())
    if grade < 4:
        failed_grades += 1
        if failed_grades >= 2:
            print(f"{name} has been excluded at {current_class} grade")
            break
        continue

    current_class += 1
    average_grade += grade
    if current_class > 12:
        break

if failed_grades < 2:
    print(f"{name} graduated. Average grade: {average_grade / 12:.2f}")
