from src.compose import compose


def add_1(x: int) -> int:
    return x + 1


def divide_by_2(y: int) -> float:
    return y / 2


def test_compose() -> None:
    my_composed_function = compose(add_1, divide_by_2)
    assert my_composed_function(5) == divide_by_2(add_1(5))
