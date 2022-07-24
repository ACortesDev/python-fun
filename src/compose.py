from typing import Callable, TypeVar


X = TypeVar("X")
Y = TypeVar("Y")
R = TypeVar("R")


def compose(
    f: Callable[[X], Y],
    g: Callable[[Y], R]
) -> Callable[[X], R]:
    def _composed(x: X) -> R:
        return g(f(x))
    return _composed
