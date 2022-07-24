from functools import reduce
from inspect import get_annotations
from typing import Any, Callable

from src.compose import compose


class CompositionError(Exception):
    pass


def can_be_composed(f: Callable, g: Callable) -> None:
    f_anns = get_annotations(f)
    g_anns = get_annotations(g)
    g_arg_type = next(iter(g_anns.values()))
    if f_anns["return"] != g_arg_type:
        raise CompositionError(
            f"Function {f} and function {g} cannot be composed"
        )


def pipe(value: Any, *functions: Callable) -> Any:
    """Type-safe at runtime"""
    def safe_runtime_compose(f: Callable, g: Callable) -> Callable:
        can_be_composed(f, g)
        return compose(f, g)

    return reduce(safe_runtime_compose, functions)(value)
