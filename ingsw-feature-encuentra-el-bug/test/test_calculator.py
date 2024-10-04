import pytest
from src.calculator import add, substract, multiply, divide, average


@pytest.mark.parametrize('a,b,expected', [
    (10, 20, 30),
    (15, 25, 40),
])
def test_add(a, b, expected):
    result = add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    'numbers, expected', [
    ([10, 20, 30, 40], 25),
    ([5, 15, 25], 15),
    ([], 0),
    ([1, 2, 3, 4, 5],6)
])
def test_average(numbers, expected):
    result = average(numbers)
    assert result == expected

