from typing import Iterable


def say_hello_to(name: str) -> str:
    return f"Hello {name}"


def say_hello_to_all(names: Iterable[str], exited: bool) -> None:
    for name in names:
        if not exited:
            print(f"Hello {name}")
        else:
            print(f"Hello {name}!!!")


name: str = 'Mike'
names: Iterable[str] = ['Mike', 'Jake', 'Luke']
exited: bool = True

say_hello_to(name)
say_hello_to_all(names, exited)
