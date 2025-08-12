max_bad_notes = int(input())
bad_notes_counter = 0
grade_counter = 0
average = 0
last_problem = None

while bad_notes_counter < max_bad_notes:
    task_name = input()

    if task_name == "Enough":
        print(f"Average score: {average / grade_counter:.2f}")
        print(f"Number of problems: {grade_counter}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    if grade <= 4:
        bad_notes_counter += 1

    grade_counter += 1
    average += grade
    last_problem = task_name

else:
    print(f"You need a break, {bad_notes_counter} poor grades.")

