# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/24/2020
#
# ============================================================================
#
# By using list comprehension, please write a program to print the list after 
# removing the 0th, 2nd, 4th, 6th numbers in [12,24,35,70,88,120,155].
#
# ============================================================================

def main():
	li = [12,24,35,70,88,120,155]
	print([x for (i,x) in enumerate(li) if i%2!=0 and i<=6])

if __name__=="__main__":
	main()