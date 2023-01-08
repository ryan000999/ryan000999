class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x:{self.x} \ny:{self.y}"

    def __repr__(self):
        return f"x:{self.x} \ny:{self.y}"

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    def __mul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        return Point(new_x, new_y)


point_1 = Point(1, 2)

print(point_1)

point_2 = Point(3, 4)

point_3 = point_1 + point_2
point_4 = point_1 * point_2

print("point_3 la:", point_3)
print("point_4 la:", point_4)
