import pytest
from utils import to_binary

@pytest.mark.parametrize("number, expected", [
    (0, '0b0'),
    (1, '0b1'),
    (5, '0b101'),
    (100, '0b1100100')
])
def test_to_binary_valid(number, expected):
    assert to_binary(number) == expected

@pytest.mark.parametrize("number", [-1, 101, 999])
def test_to_binary_out_of_range(number):
    with pytest.raises(ValueError):
        to_binary(number)

@pytest.mark.parametrize("number", [1.5, 20.7, "hello", None])
def test_to_binary_not_natural(number):
    with pytest.raises(TypeError):
        to_binary(number)
