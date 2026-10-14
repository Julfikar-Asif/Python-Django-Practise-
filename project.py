#Library Management System

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

p1 = Person("John Doe", 30)
p2 = Person("Jane Smith", 25)

# print(p1)
# print(p2)


class Member(Person):
    def __init__(self,name, age):
        super().__init__(name, age)
        self.borrowed_books = []


# m1= Member("Alice Johnson", 28)
# print(m1)
# print(m1.borrowed_books)


class Book:
    def __init__(self,title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Available: {self.is_available}"
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value

    
# b1= Book("Python Programming", "John Smith")
# print(b1)

class Library:
    def __init__(self):
        self.books =[]
    def add_book(self, book):
        self.books.append(book)
    def display_books(self):
        for book in self.books:
            if book.is_available:
                print(book)

    def borrow_book(self, member, book_title):
        for book in self.books:
            if book.title == book_title and book.is_available:
                book.is_available = False
                member.borrowed_books.append(book)
                print(f"{member.name} borrowed {book.title}")
                return
        print("Book not available or not found")
    
    def return_book(self, member , book_title):
        for book in member.borrowed_books:
            if book.title == book_title:
                book.is_available = True
                member.borrowed_books.remove(book)
                print(f"{member.name} returned {book.title}")
                return
        print("Book not found in member's borrowed books")

m1= Member("Alice Johnson", 28)
print(m1)
print(m1.borrowed_books)


b1= Book("Python Programming", "John Smith")
# print(b1)

lib =Library()
lib.add_book(Book("java Programming", "khjdh Smith"))
lib.add_book(Book("C++ Programming", " mark dwain"))
lib.display_books()
lib.borrow_book(m1, "java Programming")
lib.borrow_book(m1, "Python Programming")

lib.return_book(m1, "c++ Programming")
lib.display_books()