
class Apple:
	def __init__(self,color,weight,brand,mold):
		self.color = color
		self.weight = weight
		self.brand = brand
		self.mold = mold
		print('created!')

ap1 = Apple("red",100,"ふじ",1)

print(ap1.color)
print(ap1.brand)