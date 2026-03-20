class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_books(self,book):
        self.books.append(book)
        print(f"added: {book.title}")

    def show_all_books(self):
        print(f"---{self.name} library---")
        
        for book in self.books:
            book.show_book()
    

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
    def show_book(self):
        print(f"Title: {self.title}, Author: {self.author}")


library = Library("KINGDOM")

book1 = Book("Harry Potter...","J.K Rowling")
book2 = Book("the art of impossible","Steven Kotler")
book3 = Book("Abundance" , "peter and Steven")
book4 = Book("the peak performance","steven kotler")

library.add_books(book1)
library.show_all_books()