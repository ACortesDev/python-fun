import pytest

from src.pipe import pipe, CompositionError


def test_pipe() -> None:
    result = pipe(
        5,
        add_1,
        divide_by_2
    )
    assert result == divide_by_2(add_1(5))


def test_pipe_errors_with_wrong_types() -> None:
    with pytest.raises(CompositionError):  # Runtime error
        _ = pipe(
            5,
            add_1,
            divide_by_2,
            celebrate  # <-- wrong input type!
        )


def test_pipe_errors_with_wrong_number_of_args() -> None:
    with pytest.raises(CompositionError):
        _ = pipe(
            5,
            add_1,
            subtract,  # <-- it takes two args!
            divide_by_2
        )


def add_1(x: int) -> int:
    return x + 1


def divide_by_2(y: int) -> float:
    return y / 2


def celebrate(z: str) -> str:
    return f"Congrats {z}!"


def subtract(x: int, y: int) -> int:
    return x - y
