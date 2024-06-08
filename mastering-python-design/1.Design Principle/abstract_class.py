from abc import ABC, abstractmethod

class MyInterface(ABC):
    @abstractmethod
    def do_something(self,param: str):
        pass

class MyClass(MyInterface):
    def do_something(self, param: str):
        print(f"Doing something with: '{param}'")

if __name__ == "__main__":
    my_class = MyClass()
    my_class.do_something("some param")