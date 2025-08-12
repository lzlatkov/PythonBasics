ticket_counter = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
bought_tickets = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        print(f"Total tickets: {bought_tickets}")
        print(f"{student_tickets/ bought_tickets * 100:.2f}% student tickets.")
        print(f"{standard_tickets / bought_tickets * 100:.2f}% standard tickets.")
        print(f"{kid_tickets / bought_tickets * 100:.2f}% kids tickets.")
        break
    capacity = int(input())
    ticket_counter = 0
    while ticket_counter < capacity:
        ticket_type = input()
        if ticket_type == "End":
            break
        ticket_counter += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        bought_tickets = kid_tickets + standard_tickets + student_tickets
    print(f"{movie_name} - {ticket_counter / capacity * 100:.2f}% full.")

