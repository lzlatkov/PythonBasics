length = int(input())
width = int(input())
cake_pieces_taken = 0

total_pieces = length * width

while total_pieces >= cake_pieces_taken:
    cake_pieces = input()
    if cake_pieces == "STOP":
        print(f"{total_pieces - cake_pieces_taken} pieces are left.")
        break

    cake_pieces = int(cake_pieces)
    cake_pieces_taken += cake_pieces

else:
    print(f"No more cake left! You need {abs(cake_pieces_taken - total_pieces)} pieces more.")



