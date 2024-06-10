import math
#from typing import Protocol
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle:
    def __init__(self,width : float,height : float) -> None:
        self.width : float = width
        self.height : float = height
    
    # def area(self) -> float:
    #     return self.width * self.height
    
class Circle:
    def __init__(self,radius: float) -> None:
        self.radius : float = radius
    
    def area(self) -> float:
        return math.pi * (self.radius ** 2)
    
def calculate_area(shape : Shape) -> float:
    return shape.area()

if __name__ == "__main__":
    rect = Rectangle(12,8)
    rect_area = calculate_area(rect)
    print(f"Rectangle area: {rect_area}")

    cir = Circle(5)
    cir_area = calculate_area(cir)
    print(f"Circle area: {cir_area}")