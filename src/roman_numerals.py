from typing import Callable

from src.pipe import pipe


def replace(old: str, new: str) -> Callable[[str], str]:
    def _replace(x: str) -> str:
        return x.replace(old, new)
    return _replace


def roman_numerals(number: int) -> str:
    return pipe(
        "I" * number,
        replace("IIIII", "V"),
        replace("VV", "X"),
        replace("XXXXX", "L"),
        replace("LL", "C"),
        replace("CCCCC", "D"),
        replace("DD", "M"),
        # You can easily add new segments :)
        replace("VIIII", "IX"),
        replace("IIII", "IV"),
        replace("LXXXX", "XC"),
        replace("DCCCC", "CM")
    )
