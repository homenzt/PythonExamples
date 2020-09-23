# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/23/2020
#
# ============================================================================
#
# Please write a program to randomly generate a list with 5 numbers, which are 
# divisible by 5 and 7 , between 1 and 1000 inclusive.
#
# ============================================================================

import random

def main():
	rand = random.sample([i for i in range(1,1000) if i%5==0 and i%7==0],5)
	print(rand)

if __name__=="__main__":
	main()