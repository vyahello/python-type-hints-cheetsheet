from typing import (
    Any, List, Tuple, Set, Dict,
    Iterable, Union, Optional,
    Generator, Callable, NoReturn
)


_list: List[int] = [1, 2, 3]
_tuple: Tuple[int, str, float] = (2, 'foo', 0.1)
_tuple_range: Tuple[int, ...] = tuple(range(100))
_dict: Dict[int, bool] = {1: True}
_set: Set[str] = {'foo', 'bar'}


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


def sum_of_callable(callable_param: Callable[[int], Iterable[int]], rng: int = 5) -> int:
    return sum(callable_param(rng))


def never_return_value() -> NoReturn:
    raise RuntimeError('Never return a value!')


print(double_itself(2))
print(double_itself(2.0))
print(double_itself('2'))

print(square_of(3))
print(square_of(3.0))

print(length_of())
print(length_of('foo'))

print(sum_of([1, 2, 3]))
print(sum_of({1, 2, 3}))
print(sum_of((1, 2, 3)))

print(generator_range(5))

print(sum_of_callable(lambda x: range(x), 10))

never_return_value()
