book1 = {"ID": 1, "Name": "Harry Potter", "Author": "J.K. Rowling", "Year": "1997", "Genre": "Fantasy", "ISBN": "978-3-16-148410-0"}
book2 = {"ID": 2,"Name": "The Hobbit", "Author": "J.R.R. Tolkien", "Year": "1937", "Genre": "Fantasy", "ISBN": "978-3-16-148410-1"}
book3 = {"ID": 3,"Name": "The Catcher in the Rye", "Author": "J.D. Salinger", "Year": "1951", "Genre": "Fiction", "ISBN": "978-3-16-148410-2"}
all_books = [book1, book2, book3]
def library(book):
    input = book
    print("Hello from book.py!")
    print(input)
    if isinstance(input, int):
        return all_books[int(input)-1]
    elif isinstance(input, str):
        for book in all_books:
            if input in book.values():
                return book
    else:
        return "Invalid book."