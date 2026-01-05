import pytest

from app.split_integer import split_integer


def test_returns_correct_number_of_parts() -> None:
    value = 10
    parts = 3
    result = split_integer(value, parts)
    assert len(result) == parts


def test_sum_of_parts_equals_value() -> None:
    value = 17
    parts = 4
    result = split_integer(value, parts)
    assert sum(result) == value


def test_result_is_sorted_ascending() -> None:
    result = split_integer(32, 6)
    assert result == sorted(result)


def test_max_min_difference_not_more_than_one() -> None:
    result = split_integer(32, 6)
    assert max(result) - min(result) <= 1


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ],
)
def test_examples(value: int, parts: int, expected: list[int]) -> None:
    assert split_integer(value, parts) == expected


def test_value_equals_parts_returns_ones() -> None:
    value = 7
    parts = 7
    assert split_integer(value, parts) == [1] * parts
