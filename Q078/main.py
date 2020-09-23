# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/23/2020
#
# ============================================================================
#
# Please write a program to shuffle and print the list [3,6,7,8].
#
# ============================================================================

from random import shuffle

def main():
	li = [3,6,7,8]
	shuffle(li)
	print(li)

if __name__=="__main__":
	main()