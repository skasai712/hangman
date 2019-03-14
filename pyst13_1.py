
class Shape():
	def what_am_i(self):
		print("I am a shape.")

class Rectangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def calculate_perimeter(self):
		return (self.width + self.height) *2


class Square(Shape):
	def __init__(self, side):
		self.side = side

	def calculate_perimeter(self):
		return self.side * 4

	def change_size(self,delta_side):
		self.side += delta_side

a_rectangle = Rectangle(3,4)
a_square = Square(4)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())
a_square.change_size(3)
print(a_square.calculate_perimeter())

a_rectangle.what_am_i()
a_square.what_am_i()