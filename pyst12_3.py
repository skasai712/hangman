import math

class Triangle():

	def __init__(self,width,height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height / 2

a_triangle = Triangle(4,5)

print(a_triangle.width)
print(a_triangle.height)
print(a_triangle.area())
