class Goat:
    legs_number = 4  # type: int

    def __init__(self, height,  # type: int
                 weight,  # type: int
                 hungry  # type: int
                 ):
        # type: (int, int, bool) -> None
        self._height = height  # type: int
        self._weight = weight  # type: int
        self._hungry = hungry  # type: bool

    def stats(self):
        # type: () -> str
        return f"Goat has {self._height} height and {self._weight} weight!"

    def feed_with(self, food  # type: str
                  ):
        # type: (str) -> str
        if self._hungry:
            return f"Goat is fed up with {food}"
        return "Goat is not hungry"
