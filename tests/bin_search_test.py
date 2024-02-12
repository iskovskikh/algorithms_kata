import pytest

from algorithms_kata.bin_search import bin_search


@pytest.mark.parametrize(
    "needle,haystack,expected",
    [
        (3, [0, 1, 2, 3], 3),
        (0, [0, 1, 2, 3], 0),
        (1, [1, ], 0),
    ]
)
def test_bin_search(needle, haystack, expected):
    assert bin_search(needle, haystack) == expected


def test_bin_searc_none():
    assert bin_search(0, []) is None
