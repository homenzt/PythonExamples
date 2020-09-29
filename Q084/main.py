# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/24/2020
#
# ============================================================================
#
# By using list comprehension, please write a program generate a 3*5*8 3D array 
# whose each element is 0.
#
# ============================================================================

def main():
	w,h,l = 8,5,3
	li = [[[0 for x in range(w)] for y in range(h)] for z in range(l)]

if __name__=="__main__":
	main()