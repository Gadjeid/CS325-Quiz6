from abc import ABC , abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def display(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def display(self):
        if self.length == self.width:
            print(f"Square with length and witch {self.length}")
        else:
            print(f"Rectangle with length {self.length} and width {self.width}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * 3.14

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def display(self):
        print(f"Circle with radius {self.radius}")

class Triangle(Shape):
    def __init__(self, base, height, s1, s2, s3):
        self.base = base
        self.height = height
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def area(self):
        return self.base * self.height * (1/2)
    
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    
    def display(self):
        print(f"Triangle with base {self.base}, height {self.height}, and sides {self.s1}, {self.s2}, {self.s3}")

def main():
    circle = Circle(radius=5)
    rectangle = Rectangle(length=6, width=7)
    square = Rectangle(length=4, width=4)
    triangle = Triangle(base=3, height=6, s1=3, s2=4, s3=5)


    shapes = [rectangle, circle, square, triangle]
    for shape in shapes:
        shape.display()
        print(f"Area: {shape.area():.{2}f}")
        print(f"Perimeter: {shape.perimeter():.{2}f}\n")

if __name__ == "__main__":
    main()