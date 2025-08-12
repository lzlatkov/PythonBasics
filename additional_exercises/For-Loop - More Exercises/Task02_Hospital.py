# read user input
period_of_days = int(input())
doctor_count = 7
treated_patients_count = 0
untreated_patients_count = 0

# logic
for days in range(1, period_of_days + 1):
    patients = int(input())
    if days % 3 == 0 and untreated_patients_count > treated_patients_count:
        doctor_count += 1
    if patients <= doctor_count:
        treated_patients_count += patients
    elif patients > doctor_count:
        treated_patients_count += doctor_count
        untreated_patients_count += patients - doctor_count


# print output
print(f"Treated patients: {treated_patients_count}.")
print(f"Untreated patients: {untreated_patients_count}.")