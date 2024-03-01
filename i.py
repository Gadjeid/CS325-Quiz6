from abc import ABC, abstractmethod
class Searchable(ABC):
    @abstractmethod
    def search_by_title(self, title):
        pass

    @abstractmethod
    def search_by_author(self, author):
        pass

    @abstractmethod
    def search_by_genre(self, genre):
        pass

class Borrowable(ABC):
    @abstractmethod
    def borrow_book(self, title, book_id, user_id):
        pass

    @abstractmethod
    def return_book(self, title, book_id, user_id):
        pass

class ReportGenerator(ABC):
    @abstractmethod
    def generate_borrowing_report(self):
        pass

    @abstractmethod
    def generate_overdue_report(self):
        pass

    @abstractmethod
    def generate_popularity_report(self):
        pass

class Catalog(Searchable):
    def __init__(self, books):
        self.books = books
    def search_by_title(self, title):
        title_check = title.lower()
        print(f"Searching for books with title: {title}")
        for book in self.books:
            book_check = book['title'].lower()
            if title_check == book_check:
                print(f"{book['title']}:{book['author']}:{book['genre']}")


    def search_by_author(self, author):
        author_check = author.lower()
        print(f"Searching for books by author: {author}")
        for book in self.books:
            book_check = book['author'].lower()
            if author_check == book_check:
                print(f"{book['title']}:{book['author']}:{book['genre']}")

    def search_by_genre(self, genre):
        genre_check = genre.lower()
        print(f"Searching for books in genre: {genre}")
        for book in self.books:
            book_check = book['genre'].lower()
            if genre_check == book_check:
                print(f"{book['title']}:{book['author']}:{book['genre']}")

class BorrowManager(Borrowable):
    def borrow_book(self, title, book_id, user_id):
        print(f"User {user_id} borrowed book with ID {book_id} ({title})")

    def return_book(self, title, book_id, user_id):
        print(f"User {user_id} returned book with ID {book_id} ({title})")

    

class ReportManager(ReportGenerator):
    def generate_borrowing_report(self):
        print("Generating borrowing report")

    def generate_overdue_report(self):
        print("Generating overdue report")

    def generate_popularity_report(self):
        print("Generating popularity report")

def main():
    books = [
        {'title': 'Don Quixote', 'author': 'Miguel de Cervantes', 'genre': 'novel', 'book_id': 212},
        {'title': 'Animal Farm', 'author': 'George Orwell', 'genre': 'allegory', 'book_id': 192},
    ]

    catalog = Catalog(books)
    borrow_manager = BorrowManager()
    report_manager = ReportManager()

    # For General Guest/User
    catalog.search_by_title("Don Quixote")
    catalog.search_by_author("George Orwell")
    catalog.search_by_genre("Novel")

    borrow_manager.return_book("Animal Farm", 192, 800723461)
    borrow_manager.borrow_book("Don Quioxte", 212, 800723461)

    # For Librarian
    report_manager.generate_borrowing_report()
    report_manager.generate_overdue_report()
    report_manager.generate_popularity_report()
    
if __name__ == "__main__":
    main()