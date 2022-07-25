from src.pipe import pipe


def think_of_a_number(number: int) -> float:
    def add_one(x: int) -> int: return x + 1
    def square_it(x: int) -> int: return x * x
    def subtract_one(x: int) -> int: return x - 1
    def divide_by_the_number(x: int) -> float: return x / number
    def subtract_the_number(x: float) -> float: return x - number

    return pipe(
        number,
        add_one,
        square_it,
        subtract_one,
        divide_by_the_number,
        subtract_the_number
    )
