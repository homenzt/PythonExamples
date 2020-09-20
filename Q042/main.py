# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/20/2020
#
# ============================================================================
#
# Write a program which can map() and filter() to make a list whose elements 
# are square of even number in [1,2,3,4,5,6,7,8,9,10].
#
# ============================================================================

def even(n):
	if n%2 == 0:
		return True
	else:
		return False

def sqr(n):
	return n**2

def main():
	li = [1,2,3,4,5,6,7,8,9,10]
	li = filter(even, li)
	results = map(sqr, li)
	print(list(results))

if __name__=="__main__":
	main()