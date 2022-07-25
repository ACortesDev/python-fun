import pytest

from src.roman_numerals import roman_numerals


@pytest.mark.parametrize(
    "number,expected",
    [
        (4, "IV"),
        (11, "XI"),
        (789, "DCCLXXXIX"),
        (1954, "MCMLIV"),
    ]
)
def test_roman_numerals(number: int, expected: str) -> None:
    assert roman_numerals(number) == expected
