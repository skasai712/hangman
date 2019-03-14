import math

class Circle():

	def __init__(self,diameter):
		self.diameter = diameter

	def area(self):
		return (self.diameter / 2 ) ** 2 * math.pi 

a_circle = Circle(4)

print(a_circle.diameter)
print(a_circle.area())
a_circle.diameter = 5
print(a_circle.diameter)
print(a_circle.area())