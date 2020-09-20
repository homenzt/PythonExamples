# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/20/2020
#
# ============================================================================
#
# Write a program which can map() to make a list whose elements are square of 
# elements in [1,2,3,4,5,6,7,8,9,10].
#
# ============================================================================

def sqr(n):
	return n**2

def main():
	li = [1,2,3,4,5,6,7,8,9,10]
	result = list(map(sqr, li))
	print(result)

if __name__=="__main__":
	main()