# code don't follow LSP
class UnsupportedOperationException(Exception):
    def __init__(self, message) -> None:
        self.message = message
    
    def __str__(self) -> str:
        return self.message
    
class Bird:
    def fly(self):
        pass

class Eagle(Bird):
    def fly(self):
        print("eagle is flying ...")

class Penguin(Bird):
    def fly(self):
        raise UnsupportedOperationException("Penguin can't fly ...")

# code that follow LSP
from abc import ABC,abstractmethod

class CanFly(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird:
    def __init__(self,name) -> None:
        self.name = name

class Eagle(Bird,CanFly):
    def fly(self):
        print(f"{self.name} is flying")

class Penguin(Bird):
    pass

if __name__ =="__main__":
    eagle = Eagle("eagle")
    eagle.fly()

    penguin = Penguin("penguin")