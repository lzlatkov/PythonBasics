opened_tabs = int(input())
salary = int(input())

for _ in range(opened_tabs):
    site = input()

    if site == "Facebook":
        salary -= 150
    elif site == "Instagram":
        salary -= 100
    elif site == "Reddit":
        salary -= 50

    if salary <= 0:
        print(f"You have lost your salary.")
        break
else:
    print(salary)