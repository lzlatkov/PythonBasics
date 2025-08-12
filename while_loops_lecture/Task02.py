username = input()
password = input()

while True:
    user_input = input()
    if user_input == 1234:
        break
    user_input = input()

    print(f"Welcome {username}!")

#########################

username = input()
password = input()

user_input = input()

while user_input != password:
    user_input = input()

print(f"Welcome {username}!")#