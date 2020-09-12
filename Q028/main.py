# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/12/2020
#
# ============================================================================
#
# Define a function that can receive two integer numbers in string form and 
# compute their sum and then print it in console.
#
# ============================================================================

def adder(a,b):
	return int(a) + int(b)

def main():
	print(adder("57","48"))
	
if __name__=="__main__":
	main()