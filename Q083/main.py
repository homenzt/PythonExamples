# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/24/2020
#
# ============================================================================
#
# By using list comprehension, please write a program to print the list after 
# removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].
#
# ============================================================================

def main():
	li = [12,24,35,70,88,120,155]
	print(li)
	print([x for (i,x) in enumerate(li) if i not in range(1,4)])

if __name__=="__main__":
	main()