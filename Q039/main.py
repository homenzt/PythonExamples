# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/20/2020
#
# ============================================================================
#
# Write a program to generate and print another tuple whose values are even 
# numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
#
# ============================================================================

def main():
	toople = (1,2,3,4,5,6,7,8,9,10)
	evens = list()
	for i in toople:
		if i%2 == 0:
			evens.append(i)

	print(tuple(evens))
	
if __name__=="__main__":
	main()