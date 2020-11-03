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
