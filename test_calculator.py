import pytest
from calculator import addition


def test_addition_positive_numbers():
    assert addition(2, 3) == 5


def test_addition_negative_numbers():
    assert addition(-4, -6) == -10


def test_addition_mixed_sign():
    assert addition(-3, 7) == 4


def test_addition_floats():
    assert addition(1.5, 2.5) == pytest.approx(4.0)


def test_addition_zero():
    assert addition(0, 5) == 5
    assert addition(5, 0) == 5


def test_addition_strings():
    assert addition("hello", " world") == "hello world"
