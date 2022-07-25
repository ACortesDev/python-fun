from typing import Callable

from src.pipe import pipe


def fizzbuzz(input: list[int]) -> list[int | str]:
    return pipe(
        input,
        _map(_fizzbuzz)
    )


def _fizzbuzz(number: int) -> str:
    return pipe(
        number,
        _carbonate(15, "FizzBuzz"),
        _carbonate(3, "Fizz"),
        _carbonate(5, "Buzz"),
        _carbonate(1, str(number))  # <-- carbonateRemaining
    )


def _carbonate(divisor: int, label: str) -> Callable[[int | str], int | str]:
    def _partial(number: int | str) -> int | str:
        if isinstance(number, str):
            return number
        return label if number % divisor == 0 else number
    return _partial


def _map(f: Callable[[int], str]) -> Callable[[list], list]:
    def _partial(input: list) -> list:
        return list(map(f, input))
    return _partial
