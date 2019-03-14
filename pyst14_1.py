
class Shape():
	def what_am_i(self):
		print("I am a shape.")

class Square(Shape):
	square_list = []

	def __init__(self, side):
		self.side = side
		self.square_list.append(self)

	def calculate_perimeter(self):
		return self.side * 4

	def change_size(self,delta_side):
		self.side += delta_side

	def __repr__(self):
		return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)

a_square = Square(29)
print(Square.square_list)
another_square = Square(93)
print(Square.square_list)

print(a_square.calculate_perimeter())
a_square.change_size(3)
print(a_square.calculate_perimeter())

a_square.what_am_i()
