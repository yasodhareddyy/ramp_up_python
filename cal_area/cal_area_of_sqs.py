# Base class for shapes
class Shape:
    def area(self):
        pass


# Subclass for Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


# Subclass for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159265359 * (self.radius ** 2)  # Approximate value of pi


while True:
    print("Choose a shape to calculate its area:")
    print("1. Square")
    print("2. Triangle")
    print("3. Circle")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        side = float(input("Enter the side length of the square: "))
        square = Square(side)
        print(f"Area of the square: {square.area()}")
    elif choice == 2:
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        triangle = Triangle(base, height)
        print(f"Area of the triangle: {triangle.area()}")
    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        circle = Circle(radius)
        print(f"Area of the circle: {circle.area()}")
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
