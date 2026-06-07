"""Utility functions for generating random values."""

import random
import string
from typing import Any, TypeVar

T = TypeVar("T")


def random_integer(low: int = 0, high: int = 100) -> int:
    """Return a random integer between low and high (inclusive)."""
    return random.randint(low, high)


def random_choice(items: list[Any]) -> Any:
    """Return a random element from a non-empty list."""
    if not items:
        raise ValueError("items must not be empty")
    return random.choice(items)


def random_string(length: int = 8) -> str:
    """Return a random alphanumeric string of the given length."""
    if length < 0:
        raise ValueError("length must be non-negative")
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def shuffle(items: list[T]) -> list[T]:
    """Return a new list with the elements of items in a random order."""
    result = list(items)
    random.shuffle(result)
    return result
