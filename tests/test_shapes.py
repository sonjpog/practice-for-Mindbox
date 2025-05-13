import pytest
from math import pi, isclose
from geometry.shapes import Circle, Triangle, calculate_area


def test_circle_area():
    assert isclose(Circle(1).area(), pi)
    assert isclose(Circle(5).area(), 25 * pi)
    with pytest.raises(ValueError):
        Circle(-1)


def test_triangle_area():
    assert isclose(Triangle(3, 4, 5).area(), 6)
    assert isclose(Triangle(5, 5, 6).area(), 12)
    with pytest.raises(ValueError):
        Triangle(1, 1, 3)
    with pytest.raises(ValueError):
        Triangle(-1, 2, 2)


def test_right_angled():
    assert Triangle.is_right_angled(3, 4, 5)
    assert Triangle.is_right_angled(5, 12, 13)
    assert not Triangle.is_right_angled(5, 5, 5)
    assert not Triangle.is_right_angled(3, 4, 6)


def test_calculate_area():
    assert isclose(calculate_area(Circle(1)), pi)
    assert isclose(calculate_area(Triangle(3, 4, 5)), 6)
    assert isclose(calculate_area(1), pi)
    assert isclose(calculate_area((3, 4, 5)), 6)
    with pytest.raises(ValueError):
        calculate_area('invalid')
