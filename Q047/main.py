# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/21/2020
#
# ============================================================================
#
# Define a class named Circle which can be constructed by a radius. The Circle 
# class has a method which can compute the area.
#
# ============================================================================

class Circle:

	def __init__(self, r):
		self.radius = r

	def area(self):
		return 3.14*self.radius**2

def main():
	obj = Circle(2)
	print(obj.area())

if __name__=="__main__":
	main()