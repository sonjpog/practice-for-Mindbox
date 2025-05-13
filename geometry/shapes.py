import math
from abc import ABC, abstractmethod
from typing import Union


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @classmethod
    def is_right_angled(cls, *args) -> bool:
        return False


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError('Radius must be positive')
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if any(side <= 0 for side in (a, b, c)):
            raise ValueError('All sides must be positive')
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError('Invalid triangle sides')
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    @classmethod
    def is_right_angled(cls, a: float, b: float, c: float) -> bool:
        sides = sorted([a, b, c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2,
                            rel_tol=1e-9)


def calculate_area(shape: Union[Shape, float, tuple]) -> float:
    if isinstance(shape, Shape):
        return shape.area()
    elif isinstance(shape, (int, float)):
        return Circle(shape).area()
    elif isinstance(shape, tuple) and len(shape) == 3:
        return Triangle(*shape).area()
    else:
        raise ValueError('Unsupported shape type')
