[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

# Python type hints cheatsheet
> Implementation of python type annotations cheatsheet which is aimed on helping to comprehend python type annotations by newcomers.

## Tools

### Language(s)
- python 3.6, 3.7, 3.8, 3.9

### Development
- [black](https://black.readthedocs.io/en/stable/) code formatter

## Table of contents
- [Type comments](#type-comments)
- [Type annotations](#type-annotations)
- [The typing module](#the-typing-module)
- [Mypy static type checker tool](#mypy-static-type-checker-tool)

### Type comments
Type comments variables
```python
# type_comments_vars.py

var = 1  # type: int
var1, var2, var3 = [], (), {}  # type: list, tuple, dict


for number in range(5):  # type: int
    print(number)


for key, value in dict(a=1, b=2).items():  # type: str, int
    print(key, value)


other_var = {}  # type: ignore


def func():
    func_var = 0.3  # type: float
    print(func_var)


class A:
    class_var = "foo"  # type: str

    def __init__(self):
        self.inst_var = 10  # type: int

    def method(self):
        method_var = 0.1  # type: float
        print(method_var)
```
Type comments functions
```python
# type_comments_funcs.py

def say_hello_to(
    name,  # type: str
):
    # type: (str) -> str
    return f"Hello {name}!"
```
Type comments methods
```python
# type_comments_methods.py

class Goat:
    legs_number = 4  # type: int

    def __init__(
        self,
        height,  # type: int
        weight,  # type: int
        hungry,  # type: int
    ):
        # type: (int, int, bool) -> None
        self._height = height  # type: int
        self._weight = weight  # type: int
        self._hungry = hungry  # type: bool

    def stats(self):
        # type: () -> str
        return f"Goat has {self._height} height and {self._weight} weight!"

    def feed_with(
        self, food  # type: str
    ):
        # type: (str) -> str
        if self._hungry:
            return f"Goat is fed up with {food}"
        return "Goat is not hungry"
```
Type comments with custom types
```python
# type_comments_custom.py

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
```

### Type annotations
Type annotations are available starting from `python 3.5`.

Annotate variables
```python
# annotate_vars.py

var: int = 10
var1: list = []
var2: dict = {}


def func():
    func_var: float = 0.3
    print(func_var)


class A:
    class_var: str = "foo"

    def __init__(self):
        self.inst_var: int = 10

    def method(self):
        method_var: float = 0.1
        print(method_var)
```

Annotate functions
```python
# annotate_funcs.py

def say_hello_to(name: str) -> str:
    return f"Hello {name}!"


print(say_hello_to.__annotations__)
```

Annotate methods
```python
# annotate_methods.py

class Goat:
    legs_number: int = 4

    def __init__(self, height: int, weight: int, hungry: bool) -> None:
        self._height: int = height
        self._weight: int = weight
        self._hungry: bool = hungry

    def stats(self) -> str:
        return f"Goat has {self._height} height and {self._weight} weight!"

    def feed_with(self, food: str) -> str:
        if self._hungry:
            return f"Goat is fed up with {food}"
        return "Goat is not hungry"


goat: Goat = Goat(60, 40, True)
print(goat.__annotations__)
print(goat.__init__.__annotations__)
print(goat.stats.__annotations__)
print(goat.feed_with.__annotations__)
```

Annotate with custom types
```python
# annotate_custom_types.py

class Book:
    def __init__(self, name: str) -> None:
        self._name: str = name

    def title(self) -> str:
        return f"{self._name} book"


class Table:
    def __init__(self, book: Book) -> None:
        self._book: Book = book

    def content(self) -> str:
        return f'Table has "{self._book.title()}"'


book: Book = Book("Python type annotations")
table: Table = Table(book)
print(table.__init__.__annotations__)
print(table.content.__annotations__)
```

### The typing module
Generic built-in types
```python
# basic_types.py

from typing import (
    Any,
    List,
    Tuple,
    Set,
    Dict,
    Iterable,
    Union,
    Optional,
    Generator,
    Callable,
    NoReturn,
)


_list: List[int] = [1, 2, 3]
_tuple: Tuple[int, str, float] = (2, "foo", 0.1)
_tuple_range: Tuple[int, ...] = tuple(range(100))
_dict: Dict[int, bool] = {1: True}
_set: Set[str] = {"foo", "bar"}


def double_itself(param: Any) -> Any:
    return param * 2


def square_of(param: Union[int, float]) -> Union[int, float]:
    return param ** 2


def length_of(param: Optional[str] = None) -> Optional[int]:
    if param:
        return len(param)


def sum_of(itr: Iterable[int]) -> int:
    return sum(itr)


def generator_range(param: int) -> Generator[int, None, None]:
    yield from range(param)


def sum_of_callable(
    callable_param: Callable[[int], Iterable[int]], rng: int = 5
) -> int:
    return sum(callable_param(rng))


def never_return_value() -> NoReturn:
    raise RuntimeError("Never return a value!")


print(double_itself(2))
print(double_itself(2.0))
print(double_itself("2"))

print(square_of(3))
print(square_of(3.0))

print(length_of())
print(length_of("foo"))

print(sum_of([1, 2, 3]))
print(sum_of({1, 2, 3}))
print(sum_of((1, 2, 3)))

print(generator_range(5))

print(sum_of_callable(lambda x: range(x), 10))

never_return_value()
```

Type aliases
```python
# type_aliases.py

from typing import List, Union

Vector = List[Union[int, float]]


def scale(scalar: int, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


print(scale(2, [0.1, 0.2, 0.3]))
```

Create own type
```python
# own_type.py

from typing import List, NewType, TypeVar

Position = NewType("Position", int)
IntOrStr = TypeVar("IntOrStr", int, str)

some_position = Position(10) + Position(7)


def count_number_of_element(
    container: List[IntOrStr], element: IntOrStr
) -> int:
    return container.count(element)


print(some_position)
print(count_number_of_element([1, 1, 2, "foo", "bar", 1], 1))
```

### Mypy static type checker tool
Install mypy
```bash
pip install mypy
```
Sample mypy configuration file
```text
# mypy.ini

[mypy]
python_version = 3.6
warn_no_return = True
warn_return_any = True
warn_unused_configs = True
disallow_any_expr = True
show_column_numbers = True
show_error_context = True
```

```python
# hello.py
from typing import Iterable


def say_hello_to(name: str) -> str:
    return f"Hello {name}"


def say_hello_to_all(names: Iterable[str], exited: bool) -> None:
    for name in names:
        if not exited:
            print(f"Hello {name}")
        else:
            print(f"Hello {name}!!!")


name: str = "Mike"
names: Iterable[str] = ["Mike", "Jake", "Luke"]
exited: bool = True

say_hello_to(name)
say_hello_to_all(names, exited)
```
Validate types with mypy
```bash
mypy -h
mypy hello.py
```

## Development notes

### Additional materials
- [https://docs.python.org/3/library/typing.html](https://docs.python.org/3/library/typing.html)
- [https://www.python.org/dev/peps/pep-0483](https://www.python.org/dev/peps/pep-0483)
- [https://www.python.org/dev/peps/pep-0484](https://www.python.org/dev/peps/pep-0484)
- [https://www.python.org/dev/peps/pep-0526](https://www.python.org/dev/peps/pep-0526)
- [https://mypy.readthedocs.io/en/latest](https://mypy.readthedocs.io/en/latest)
- [https://github.com/python/mypy](https://github.com/python/mypy)

### Meta
Author – Volodymyr Yahello.

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. Create your feature branch (git checkout -b feature/fooBar)
5. Commit your changes (git commit -am 'Add some fooBar')
6. Push to the branch (git push origin feature/fooBar)
7. Create a new Pull Request
