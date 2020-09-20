# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/20/2020
#
# ============================================================================
#
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the 
# first half values in one line and the last half values in one line.
#
# ============================================================================

def main():
	toople = (1,2,3,4,5,6,7,8,9,10)
	half = int(len(toople)/2)
	print(toople[:half])
	print(toople[half:])
	
if __name__=="__main__":
	main()