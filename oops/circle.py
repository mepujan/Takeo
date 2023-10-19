class Circle:
    PI = 3.14

    def __init__(self, radius) -> None:
        self.radius = radius

    # calculate the area of circle
    def calculate_area(self):
        ''' Returns the area of circle'''
        return self.PI * self.radius ** 2

    # calculate the perimeter of circle
    def calculate_perimeter(self):
        '''Returns the perimeter of circle'''
        return 2 * self.PI * radius


radius = float(input("Enter the radius of circle: "))
circle = Circle(radius)
print("Area of Circle is : ", round(circle.calculate_area(), 2))
print("Perimeter of Circle is: ", round(circle.calculate_perimeter(), 2))
