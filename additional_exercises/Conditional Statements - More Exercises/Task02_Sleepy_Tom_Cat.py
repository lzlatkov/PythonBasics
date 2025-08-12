#Read user input
GOOD_REST = 30_000
DAYS_PER_YEAR = 365
WORKING_DAYS_PLAY_TIME = 63
NON_WORKING_DAYS_PLAY_TIME = 127

non_working_days = int(input())

#Logic
working_days = DAYS_PER_YEAR - non_working_days

total_working_days_playtime = WORKING_DAYS_PLAY_TIME * working_days
total_non_working_days_playtime = NON_WORKING_DAYS_PLAY_TIME * non_working_days
playtime_total = total_working_days_playtime + total_non_working_days_playtime

if playtime_total > GOOD_REST:
    print("Tom will run away")
    print(f"{(playtime_total - GOOD_REST) // 60} hours and {(playtime_total - GOOD_REST) % 60} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{(GOOD_REST - playtime_total) // 60} hours and {(GOOD_REST - playtime_total) % 60} minutes less for play")

