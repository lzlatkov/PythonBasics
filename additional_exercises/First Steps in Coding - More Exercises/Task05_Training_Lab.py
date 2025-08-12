#Read user input
corridor_width = 1
length = float(input())
width = float(input()) - corridor_width
area = 0
working_spaces_taken = 3
working_space_width = 0.7
working_space_lenght = 1.2

#Logic
area = length * width
total_working_space_width_taken = width // working_space_width
total_working_space_lenght_taken = length // working_space_lenght

total_working_spaces = total_working_space_width_taken * total_working_space_lenght_taken - 3

print(total_working_spaces)