from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Hinh tron co ban kinh la:{self.radius}"

    def __repr__(self) -> str:
        return f"Hinh tron co r = {self.radius}"

    @property
    def get_radius(self):
        return f"Ban kinh hinh tron la r = {self.radius}"

    def set_radius(self, r):
        self.radius = r

    @property
    def get_area(self):
        return pi * self.radius**2
    
circle_1 = Circle(3.5)

print(circle_1)
print(repr(circle_1))
print(circle_1.get_radius)
print(circle_1.get_area)
circle_1.set_radius(3)
print(circle_1.get_area)