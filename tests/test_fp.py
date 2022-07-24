import pytest

from src.compose import compose
from src.pipe import pipe, CompositionError


def add_1(x: int) -> int:
    return x + 1


def divide_by_2(y: int) -> float:
    return y / 2


def celebrate(z: str) -> str:
    return f"Congrats {z}!"


def test_compose() -> None:
    my_composed_function = compose(add_1, divide_by_2)
    assert my_composed_function(5) == divide_by_2(add_1(5))


def test_pipe() -> None:
    result = pipe(
        5,
        add_1,
        divide_by_2
    )

    assert result == divide_by_2(add_1(5))

    with pytest.raises(CompositionError): # Runtime error
        _ = pipe(
            5,
            add_1,
            divide_by_2,
            celebrate  # <-- mypy won't complain
        )
