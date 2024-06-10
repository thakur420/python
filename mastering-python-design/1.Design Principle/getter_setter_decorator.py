class Circle:
    def __init__(self,radius:int) -> None:
        self._radius = radius
    
    @property
    def radius(self): # getter method
        return self._radius
    
    @radius.setter
    def radius(self,val :int): #setter method
        if val < 0:
            raise ValueError("Radius can't be negative")
        self._radius = val

if __name__ == "__main__":
    circle = Circle(10)
    print(f"Initial Radius : {circle.radius}")
    circle.radius = 15
    print(f"New Radius : {circle.radius}")


