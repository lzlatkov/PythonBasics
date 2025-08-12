searched_book = input()
book_counter = 0

while True:
    book = input()

    if book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {book_counter} books.")
        break

    if book == searched_book:
        print(f"You checked {book_counter} books and found it.")
        break
    book_counter += 1

