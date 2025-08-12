goal = 10_000
total_stepps = 0

while total_stepps < goal:
    steps = input()
    if steps == "Going home":
        additional_steps = int(input())
        total_stepps += additional_steps
        break

    steps = int(steps)
    total_stepps += steps

if total_stepps < goal:
    print(f"{goal - total_stepps} more steps to reach goal.")

if total_stepps >= goal:
    print(f"Goal reached! Good job!")
    print(f"{total_stepps - goal} steps over the goal!")


