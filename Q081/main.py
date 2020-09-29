# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/24/2020
#
# ============================================================================
#
# By using list comprehension, please write a program to print the list after 
# removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
#
# ============================================================================

def main():
	li = [12,24,35,70,88,120,155]
	print([i for i in li if i%5!=0 and i%7!=0])

if __name__=="__main__":
	main()