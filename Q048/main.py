# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/21/2020
#
# ============================================================================
#
# Define a class named Rectangle which can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area.
#
# ============================================================================

class Rectangle:

	def __init__(self, l, w):
		self.length = l
		self.width = w

	def area(self):
		return self.length*self.width

def main():
	obj = Rectangle(2,4)
	print(obj.area())

if __name__=="__main__":
	main()