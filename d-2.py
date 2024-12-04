import math


class Rectangle:
    # コードが期待通り動作するように実装
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return f"{self.height * self.width:.2f}"

    def diagonal(self):
        return f"{math.sqrt(self.height**2 + self.width**2):.2f}"


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
