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
    class_var = 'foo'  # type: str

    def __init__(self):
        self.inst_var = 10  # type: int

    def method(self):
        method_var = 0.1  # type: float
        print(method_var)
