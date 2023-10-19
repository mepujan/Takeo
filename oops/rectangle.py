class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # calculating the area of rectangle

    def calculate_area(self):
        area = self.height * self.width
        return area


rectangle = Rectangle(8, 5)
area = rectangle.calculate_area()
print("Area of rectangle is : ", area)
