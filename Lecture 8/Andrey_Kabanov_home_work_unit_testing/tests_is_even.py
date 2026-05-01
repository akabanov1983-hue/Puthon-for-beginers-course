import pytest
from is_even import is_even


def test_is_even_2_true():
    assert is_even(2) == True


def test_is_even_3_false():
    assert is_even(3) == False


def test_is_even_0_true():
    assert is_even(0) == True


def test_is_even_minus_1_false():
    assert is_even(-1) == False


def test_is_even_minus_2_false():
    assert is_even(-2) == True

def test_is_even_2_dot_5_false():
    assert is_even(2.5) == False

def test_is_even_minus_2_dot_5_false():
    assert is_even(-2.5) == False
