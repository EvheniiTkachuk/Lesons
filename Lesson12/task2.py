# Library
# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []


class Author:

    def __init__(self, name: str, country: str, birthday: int):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'{self.name} ({self.country}, {self.birthday})'

    def __str__(self):
        return self.name


class Book:
    count = 0

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author

    @staticmethod
    def get_count():
        return Book.count

    def __repr__(self):
        return Book.__str__(self)

    def __str__(self):
        return f'{self.name} ({self.author}, {self.year})'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author) -> Book:
        Library.add_author(self, author)
        new = Book(name, year, author)
        author.books.append(new)
        self.books.append(new)
        Book.count += 1
        return new

    @staticmethod
    def group_by_author(author: Author):
        return author.books

    @staticmethod
    def show_group_by_author(author: Author):
        print(f'Книги автора {author}:\n{Library.group_by_author(author)}')

    def show_group_by_year(self, year: int):
        print(f'Список книг за {year} год:\n{Library.group_by_year(self, year)}')

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def add_author(self, author: Author):
        if self.authors.count(author) == 0:
            self.authors.append(author)

    def __repr__(self):
        return Library.__str__(self)

    def __str__(self):
        return f'Название: {self.name}\nКниги: {self.books}\nАвторы: {self.authors}\n'


lib = Library('Александрийская')

Tolstoy = Author('Толстой', 'Россия', 1828)
Gogol = Author('Гоголь', 'Россия', 1809)
Mayakovskii = Author('Маяковский', 'Грузия', 1893)

lib.new_book('Война и мир', 1897, Tolstoy)
lib.new_book('Анна Каренина', 1877, Tolstoy)
lib.new_book('Мертвые души', 1842, Gogol)
lib.new_book('Облако в штанах', 1915, Mayakovskii)
lib.new_book('Флейта - позвоночник', 1915, Mayakovskii)
print(lib)

lib.show_group_by_author(Tolstoy)
print()
lib.show_group_by_year(1915)
print()
print(f'Общее количество книг в библиотеке: {Book.get_count()}')
