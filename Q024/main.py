# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/09/2020
#
# ============================================================================
#
# Python has many built-in functions, and if you do not know how to use it, 
# you can read document online or find some books. But Python has a built-in 
# document function for every built-in functions.
#
# Please write a program to print some Python built-in functions documents, 
# such as abs(), int(), raw_input()
#
# And add document for your own function
#
# ============================================================================

def printer():
	"""Printer prints the docstrings for abs(), int(), and input()"""
	print("abs() docstring: \n", abs.__doc__)
	print("\nint() docstring: \n",int.__doc__)
	print("\ninput() docstring: \n",input.__doc__)
	print("\nThis script docstring: \n",printer.__doc__)

def main():
	printer()
	
if __name__=="__main__":
	main()