class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self) -> None:
        self.engine = Engine()
    
    def start(self):
        self.engine.start()
        print("Car Started")

if __name__ == "__main__":
    my_car = Car()
    my_car.start()