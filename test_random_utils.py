"""Tests for random_utils module."""

import pytest
from random_utils import random_integer, random_choice, random_string, shuffle


def test_random_integer_in_range():
    for _ in range(50):
        value = random_integer(1, 10)
        assert 1 <= value <= 10


def test_random_integer_default_range():
    for _ in range(50):
        value = random_integer()
        assert 0 <= value <= 100


def test_random_choice_returns_element():
    items = [1, 2, 3, 4, 5]
    for _ in range(20):
        assert random_choice(items) in items


def test_random_choice_empty_raises():
    with pytest.raises(ValueError):
        random_choice([])


def test_random_string_length():
    for length in [0, 1, 8, 16]:
        result = random_string(length)
        assert len(result) == length


def test_random_string_alphanumeric():
    result = random_string(100)
    assert result.isalnum()


def test_random_string_negative_raises():
    with pytest.raises(ValueError):
        random_string(-1)


def test_shuffle_contains_same_elements():
    items = [1, 2, 3, 4, 5]
    result = shuffle(items)
    assert sorted(result) == sorted(items)


def test_shuffle_does_not_modify_original():
    items = [1, 2, 3]
    original = list(items)
    shuffle(items)
    assert items == original
