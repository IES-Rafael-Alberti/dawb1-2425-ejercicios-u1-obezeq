import pytest
from src.suma import suma

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (0, 0, 0),
        (-1, 1, 0),
        (5, 5, 10)
    ]
)

def test_suma_params(input_x, input_y, expected):
    assert suma(input_x, input_y) == expected