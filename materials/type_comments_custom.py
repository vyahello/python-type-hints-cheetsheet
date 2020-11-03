class Book:
    def __init__(
        self, name  # type: str
    ):
        # type: (str) -> None
        self._name = name  # type: str

    def title(self):
        # type: () -> str
        return f"{self._name} book"


class Table:
    def __init__(
        self, book  # type: Book
    ):
        # type: (Book) -> None
        self._book = book  # type: Book

    def content(self):
        # type: () -> str
        return f'Table has "{self._book.title()}"'


book = Book("Python type annotations")  # type: Book
table = Table(book)  # type: Table
