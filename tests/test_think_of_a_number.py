import pytest

from src.think_of_a_number import think_of_a_number


@pytest.mark.parametrize("number", [5, 3, 100, -4, 42])
def test_think_of_a_number(number: int) -> None:
    assert think_of_a_number(number) == 2
