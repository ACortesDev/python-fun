from typing import Tuple
import pytest

from src.fizzbuzz import fizzbuzz


def fizzbuz_test_case(length: int) -> Tuple[list[int], list[str]]:
    """Generate test cases with the imperative FizzBuzz solution"""
    def carb(n: int) -> str:
        if n % 15 == 0:
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 == 0:
            return "Buzz"
        else:
            return str(n)  # <-- carbonateRemaining

    return list(range(length)), list(map(carb, range(length)))


@pytest.mark.parametrize(
    "input,expected",
    [
        ([1, 3, 5, 15], ["1", "Fizz", "Buzz", "FizzBuzz"]),
        fizzbuz_test_case(length=100),
        fizzbuz_test_case(length=500),
        fizzbuz_test_case(length=1000),
    ]
)
def test_fizzbuzz(input: list[int], expected: list[str]) -> None:
    assert fizzbuzz(input) == expected
