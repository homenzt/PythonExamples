# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/20/2020
#
# ============================================================================
#
# Write a program which can map() to make a list whose elements are square of 
# numbers between 1 and 20 (both included).
#
# ============================================================================

def main():
	li = map(lambda x: x**2, range(1,21))
	print(list(li))

if __name__=="__main__":
	main()