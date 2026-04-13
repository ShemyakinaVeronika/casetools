import pytest
from main_after import quadratic_equation


# Общие случаи

def test_two_roots():
    assert quadratic_equation(1, -3, 2) == [1.0, 2.0]

def test_one_root():
    assert quadratic_equation(1, 2, 1) == [-1.0]


def test_negative_discriminant():
    assert quadratic_equation(1, 0, 1) == "Действительных корней нет."


# Краевые случаи

def test_zero_b():
    assert quadratic_equation(1, 0, -4) == [-2.0, 2.0]


def test_zero_c():
    assert quadratic_equation(1, -5, 0) == [0.0, 5.0]


def test_large_numbers():
    result = quadratic_equation(1e6, -3e6, 2e6)
    assert result == [1.0, 2.0]


def test_small_numbers():
    result = quadratic_equation(0.001, -0.003, 0.002)
    assert result == [1.0, 2.0]


# Негативные случаи

def test_a_is_zero():
    assert quadratic_equation(0, 2, 1) == "Это не квадратное уравнение."


def test_invalid_type_string():
    assert quadratic_equation("a", 2, 1) == "Неверный тип коэффициентов."


def test_invalid_type_none():
    assert quadratic_equation(None, 2, 1) == "Неверный тип коэффициентов."
