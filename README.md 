#  Практическое задание для вычисления площади геометрических фигур

Тестовое задание для Mindbox


## Пример использования

```yaml
# Создание фигур напрямую
circle = Circle(5)
print(circle.area())  # 78.539...

triangle = Triangle(3, 4, 5)
print(triangle.area())  # 6.0
print(Triangle.is_right_angled(3, 4, 5))  # True

# Универсальный расчет площади
print(calculate_area(10))  # площадь круга с радиусом 10
print(calculate_area((5, 12, 13)))  # площадь треугольника
```

## Для добавления новой фигуры нужно просто создать новый класс, унаследованный от Shape и реализовать метод area(). Например, для квадрата:

```yaml
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
```
