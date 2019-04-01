from typing import List, Union
Vector = List[Union[int, float]]


def scale(scalar: int, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


print(scale(2, [0.1, 0.2, 0.3]))
