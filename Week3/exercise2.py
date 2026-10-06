# 🌟 Exercise 2: Circle
# #Create a class that represents a simple circle. A Circle can be defined by
#specifying the **radius**, and the **diameter** should be a computed property.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    def area(self):
        return math.pi * self._radius ** 2

    def __str__(self):
        return f"Circle(radius={self._radius})"

    def __repr__(self):
        return f"Circle({self._radius})"

    def __add__(self, other):
        return Circle(self._radius + other._radius)

    def __gt__(self, other):
        return self._radius > other._radius

    def __eq__(self, other):
        return self._radius == other._radius

    def __lt__(self, other):
        return self._radius < other._radius


#**Test:**

import math

c1 = Circle(5)
c2 = Circle(10)
c3 = Circle(5)

print(c1)                    # Circle(radius=5)
print(c1.diameter)           # 10
c1.diameter = 20
print(c1.radius)             # 10.0
print(f"Area: {c1.area():.2f}")

c4 = c1 + c2
print(c4)                    # Circle(radius=20.0)

print(c1 > c2)              # False (radius 10 == 10 — not greater)
print(c1 == c2)             # True  (both radius 10)
print(c1 == c3)             # False (radius 10 != 5)

circles = [Circle(8), Circle(3), Circle(12), Circle(1), Circle(5)]
for c in sorted(circles):
    print(f"  {c} — area: {c.area():.2f}")
