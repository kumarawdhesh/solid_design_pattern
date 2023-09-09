"""
Open/Closed Principle (OCP):
This principle states that a class should be open for extension but closed for modification. 
In Python, you can achieve this by using inheritance, abstract classes, and interfaces 
to allow for adding new functionality without modifying existing code.

Example in Python:

Here, the Shape class is open for extension by allowing new shapes (e.g., Circle) 
to be added without modifying the existing code.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
