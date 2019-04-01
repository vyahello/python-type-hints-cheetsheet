def say_hello_to(name: str) -> str:
    return f"Hello {name}!"


print(say_hello_to.__annotations__)
