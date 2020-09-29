# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/24/2020
#
# ============================================================================
#
# By using list comprehension, please write a program to print the list after 
# removing the value 24 in [12,24,35,24,88,120,155].
#
# ============================================================================

def main():
	li = [12,24,35,70,88,120,155]
	print([x for (i,x) in enumerate(li) if x!=24])

if __name__=="__main__":
	main()