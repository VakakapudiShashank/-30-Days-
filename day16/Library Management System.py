# Day 16: Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} - {'Available' if self.available else 'Issued'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book)


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, book: Book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")


# Demo
lib = Library()
book1 = Book("Python 101", "Guido")
book2 = Book("Data Science", "Jake")

lib.add_book(book1)
lib.add_book(book2)

member1 = Member("Alice")
member1.borrow(book1)
member1.borrow(book2)
member1.return_book(book1)

lib.show_books()
