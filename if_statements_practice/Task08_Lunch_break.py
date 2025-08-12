from math import ceil

movie_name = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length * 0.125
relax_time = break_length * 0.25

break_time_left = break_length - (lunch_time + relax_time)

if break_time_left >= episode_length:
    print(f"You have enough time to watch {movie_name} and left with {ceil(break_time_left - episode_length)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(episode_length - break_time_left)} more minutes.")