class Circle:
   def __init__(self, radius):
       print("Begin")
       self._radius = radius #attribute as private
   @property #It is a property Tag
   def radius(self):
       print("First")
       return self._radius
   @radius.setter #With the help of setter Here function are overload as well
   def radius(self, value):
       print("second")
       if value < 0:
           raise ValueError("Radius cannot be negative")
       self._radius = value
   @property
   def diameter(self):
       return 2 * self.radius
   @diameter.setter
   def diameter(self, value):
       self.radius = value / 2
   @property
   def area(self):
       return 3.14 * (self.radius ** 2)
c = Circle(5)
print(c.radius)  # Output: 5

c.radius = 10
print(c.radius)  # Output: 10
print(c.diameter)  # Output: 20

c.diameter = 30
print(c.diameter)  # Output: 30
print(c.radius)  # Output: 15

print(c.area)  # Output: 706.5
