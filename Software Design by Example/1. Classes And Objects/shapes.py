import math
class Shape:
    def __init__(self,name) -> None:
        self.name = name

    def perimeter(self):
        raise NotImplementedError("Provide implementation for perimeter")
    
    def area(self):
        raise NotImplementedError("Provide implementation for area")
    

class Square(Shape):
    def __init__(self,name,side) -> None:
        super().__init__(name)
        self.side = side
    
    def perimeter(self):
        return 4 * self.side
    
    def area(self):
        return self.side ** 2
    
class Circle(Shape):
    def __init__(self,name,radius) -> None:
        super().__init__(name)
        self.radius  = radius

    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
if __name__ == "__main__":
    shapes = [Square('sq',3), Circle('ci',2)]
    for shape in shapes:
        n = shape.name
        p = shape.perimeter()
        a = shape.area()
        print(f"{n} has perimeter {p:.2f} and area {a:.2f}")