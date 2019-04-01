class Book:
    def __init__(self, name: str) -> None:
        self._name: str = name

    def title(self) -> str:
        return f'{self._name} book'


class Table:
    def __init__(self, book: Book) -> None:
        self._book: Book = book

    def content(self) -> str:
        return f'Table has "{self._book.title()}"'


book: Book = Book('Python type annotations')
table: Table = Table(book)
print(table.__init__.__annotations__)
print(table.content.__annotations__)
