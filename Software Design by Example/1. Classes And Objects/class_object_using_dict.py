import math
# Shape class and its method
def shape_new(name):
    return {
        "name": name,
        "_class": Shape
    }
def shape_density(self,weight):
    return weight / call(self, "area")

Shape = {
    "_classname":"Shape",
    "_parent" : None,
    "_new" : shape_new,
    "density": shape_density
}

# Square class and its method
def square_perimeter(self):
    return 4 * self["side"]

def square_area(self):
    return self["side"] ** 2

def square_new(name, side):
    return make(Shape, name) | {
        "side": side,
        "_class": Square
}
Square = {
    "perimeter": square_perimeter,
    "area": square_area,
    "_classname": "Square",
    "_parent": Shape,
    "_new":square_new
}

# Circle Class and its method
def circle_perimeter(self):
    return 2 * math.pi * self["radius"]

def circle_area(self):
    return math.pi * self["radius"] ** 2

def circle_new(name,radius):
    return make(Shape,name) | {
        "radius" : radius,
        "_class" : Circle
    }
Circle = {
    "_classname" : "Circle",
    "_parent" : Shape,
    "_new" : circle_new,
    "perimeter" : circle_perimeter,
    "area" : circle_area
}
# Utility Methods for calling method and constructor
def make(cls,*args):
    return cls["_new"](*args)

def call(self,method_name,*args):
    method_name = find(self["_class"],method_name)
    return method_name(self,*args)

def find(cls,method_name):
    # print(f"cls:{cls}, method:{method_name}")
    while cls is not None:
        if method_name in cls:
            return cls[method_name]
        cls = cls["_parent"]
    raise NotImplementedError("method_name")

if __name__ == "__main__":
    shapes = [make(Square, "sq", 3), make(Circle, "ci", 2)]
    for shape in shapes:
        n = shape["name"]
        d = call(shape, "density", 5)
        print(f"{n}: {d:.2f}")