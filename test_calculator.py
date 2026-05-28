import pytest
from calculator import addition, multiplication, subtraction


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


def test_subtraction_positive_numbers():
    assert subtraction(5, 3) == 2


def test_subtraction_negative_numbers():
    assert subtraction(-4, -6) == 2


def test_subtraction_mixed_sign():
    assert subtraction(-3, 7) == -10


def test_subtraction_floats():
    assert subtraction(3.5, 1.5) == pytest.approx(2.0)


def test_subtraction_zero():
    assert subtraction(5, 0) == 5
    assert subtraction(0, 5) == -5
