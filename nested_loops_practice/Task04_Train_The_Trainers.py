grade_sum = 0
project_grade = 0
final_assessment = 0
total_projects = 0

judges_count = int(input())
while True:
    presentation_name = input()
    if presentation_name == "Finish":
        print(f"Student's final assessment is {final_assessment / total_projects:.2f}.")
        break
    project_grade = 0
    grade_sum = 0
    for _ in range(judges_count):
        grade_sum += float(input())
    project_grade = grade_sum / judges_count
    print(f"{presentation_name} - {project_grade:.2f}.")

    final_assessment += project_grade
    total_projects += 1



