from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
        super().__init__()

    def area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth
        super().__init__()

    def area(self):
        return self.length * self.breadth


circle = Circle(4)
rectangle = Rectangle(4, 5)
print("Area of circle is : ", round(circle.area(), 2))
print("Area of rectangle : ", rectangle.area())
