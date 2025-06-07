from main import Calculator
import pytest
@pytest.mark.parametrize(
    "x, y, res",
    [
        (1, 2, 0.5),
        (5, -1, -5),
    ]
                         )


def test_add(x, y, res):
    assert Calculator().add(x, y) == res


def test_divide(x, y, res):
    assert Calculator().divide(x, y) == res
