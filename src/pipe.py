from functools import reduce
from inspect import get_annotations
from typing import Any, Callable

from src.compose import compose


class CompositionError(Exception):
    def __init__(self, f: Callable, g: Callable) -> None:
        super().__init__(f"{f} and {g} cannot be composed")


def can_be_composed(f: Callable, g: Callable) -> None:
    f_annotations = get_annotations(f)
    g_annotations = get_annotations(g)
    if 2 == len(f_annotations) != len(g_annotations):
        raise CompositionError(f, g)

    _ = g_annotations.pop("return")
    _, g_input_type = g_annotations.popitem()
    f_output_type = f_annotations.pop("return")
    if f_output_type != g_input_type:
        raise CompositionError(f, g)


def pipe(value: Any, *functions: Callable) -> Any:
    """Type-safe at runtime"""
    for i in range(1, len(functions)):
        can_be_composed(functions[i-1], functions[i])
    return reduce(compose, functions)(value)
