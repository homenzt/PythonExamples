# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/09/2020
#
# ============================================================================
#
# Define a class, which have a class parameter and have a same instance 
# parameter.
#
# ============================================================================

class Bike:

	name = "Bike"

	def __init__(self, type=None):
		self.type = type

def main():
	uni = Bike("Unicycle")
	print("%s type is %s"%(Bike.name, uni.type))

	tri = Bike()
	tri.type="Tricycle"
	print("%s type is %s"%(Bike.name, tri.type))

	
if __name__=="__main__":
	main()