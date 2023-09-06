class Book:
    def __init__(self, title, author, year, genre, copies):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__genre = genre
        self.__copies = copies

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    @property
    def genre(self):
        return self.__genre

    @property
    def copies(self):
        return self.__copies

    def __str__(self):
        return f"{self.__title} by {self.__author} ({self.__year}), Genre: {self.__genre}, Copies: {self.__copies}"


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.__books.append(book)
            print(f"Added: {book.title}")

    def remove_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
            print(f"Removed: {book.title}")

    def find_books_by_author(self, author):
        author_books = [book for book in self.__books if book.author == author]
        return author_books

    def find_books_by_genre(self, genre):
        genre_books = [book for book in self.__books if book.genre == genre]
        return genre_books

    def list_all_books(self):
        return self.__books

# Пример использования:

book1 = Book('Book 1', 'Author 1', 2000, 'Genre 1', 5)
book2 = Book('Book 2', 'Author 2', 1990, 'Genre 2', 3)
book3 = Book('Book 3', 'Author 1', 2005, 'Genre 1', 2)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("All Books:")
for book in library.list_all_books():
    print(book)

print("\nBooks by Author 1:")
author1_books = library.find_books_by_author('Author 1')
for book in author1_books:
    print(book)

print("\nBooks in Genre 1:")
genre1_books = library.find_books_by_genre('Genre 1')
for book in genre1_books:
    print(book)

