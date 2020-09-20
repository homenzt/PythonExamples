# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/20/2020
#
# ============================================================================
#
# Define a class named American which has a static method called 
# printNationality.
#
# ============================================================================

class American:
	@staticmethod
	def printNationality():
		print("American")

def main():
	citizen = American()

	# This will not run if @staticmethod does not decorate the 
	# printNationality() function because the class has no instance.
	citizen.printNationality()

	# This will run even though the @staticmethod does not decorate
	# printNationality().
	American.printNationality()

if __name__=="__main__":
	main()