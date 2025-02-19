import pytest

# Assuming the Book and Library classes are defined in a file named `library.py`
from library import Book, Library

class TestBook:

    def test_book_initialization(self):
        book = Book("1984", "George Orwell", 1949, "Dystopian")
        assert book.title == "1984"
        assert book.author == "George Orwell"
        assert book.year == 1949
        assert book.genre == "Dystopian"
        assert book.checked_out == False

    def test_str_method(self):
        book = Book("1984", "George Orwell", 1949, "Dystopian")
        expected_output = "1984 by George Orwell (1949) - Genre: Dystopian"
        assert str(book) == expected_output

    def test_eq_method(self):
        book1 = Book("Age of Iron", "J.M. Coetzee", 1990, "Fiction")
        book2 = Book("Age of Iron", "J.M. Coetzee", 1990, "Fiction", True)
        assert book2 == book1
        book3 = Book("Moby Dick", "Herman Melville", 1851, "Epic")
        assert not (book3 == book1)

    def test_check_out(self):
        book = Book("1984", "George Orwell", 1949, "Dystopian")
        book.check_out()
        assert book.checked_out == True

    def test_return_book(self):
        book = Book("1984", "George Orwell", 1949, "Dystopian")
        book.check_out()
        book.return_book()
        assert book.checked_out == False

    def test_is_available(self):
        book = Book("1984", "George Orwell", 1949, "Dystopian")
        assert book.is_available() == True
        book.check_out()
        assert book.is_available() == False


class TestLibrary:

    @pytest.fixture
    def setup_library(self):
        library = Library()
        book1 = Book("1984", "George Orwell", 1949, "Dystopian")
        book2 = Book("Brave New World", "Aldous Huxley", 1932, "Dystopian")
        book3 = Book("Fahrenheit 451", "Ray Bradbury", 1953, "Science Fiction")
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)
        return library, book1, book2, book3

    def test_add_book(self, setup_library):
        library, book1, book2, book3 = setup_library
        book4 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
        library.add_book(book4)
        assert len(library.books) == 4

    def test_remove_book(self, setup_library):
        library, book1, book2, book3 = setup_library
        library.remove_book("1984")
        assert len(library.books) == 2
        assert library.find_book("1984") is None

    def test_remove_book_not_found(self, setup_library):
        library, book1, book2, book3 = setup_library
        with pytest.raises(ValueError):
            library.remove_book("The Catcher in the Rye")

    def test_find_book(self, setup_library):
        library, book1, book2, book3 = setup_library
        found_book = library.find_book("Brave New World")
        assert found_book == book2

    def test_find_book_not_found(self, setup_library):
        library, book1, book2, book3 = setup_library
        found_book = library.find_book("The Catcher in the Rye")
        assert found_book is None

    def test_list_available_books(self, setup_library):
        library, book1, book2, book3 = setup_library
        book1.check_out()
        available_books = library.list_available_books()
        assert len(available_books) == 2
        assert book2 in available_books
        assert book3 in available_books