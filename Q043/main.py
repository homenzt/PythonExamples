# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/20/2020
#
# ============================================================================
#
# Write a program which can filter() to make a list whose elements are even 
# number between 1 and 20 (both included).
#
# ============================================================================

def main():
	li = filter(lambda x: x%2 == 0, range(1,21))
	print(list(li))

if __name__=="__main__":
	main()