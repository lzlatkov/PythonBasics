#Read user input

pool_total_volume = int(input())
pipe_1_volume = int(input())
pine_2_volume = int(input())
hours_of_absence = float(input())

#Logic

pipe_1_volume_deposit = pipe_1_volume * hours_of_absence
pipe_2_volume_deposit = pine_2_volume * hours_of_absence
total_volume_deposit = pipe_1_volume_deposit + pipe_2_volume_deposit
percent_pipe_one = pipe_1_volume_deposit / total_volume_deposit
percent_pipe_two = pipe_2_volume_deposit / total_volume_deposit
total_percent = total_volume_deposit / pool_total_volume

if pool_total_volume >= total_volume_deposit:
    print(f"The pool is {total_percent * 100:.2f}% full. Pipe 1: {percent_pipe_one * 100:.2f}%. Pipe 2: {percent_pipe_two * 100:.2f}%.")
else:
    print(f"For {hours_of_absence} hours the pool overflows with {total_volume_deposit - pool_total_volume} liters.")

