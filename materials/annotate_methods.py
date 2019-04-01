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
