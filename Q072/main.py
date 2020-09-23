# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/23/2020
#
# ============================================================================
#
# Please write a program to generate a list with 5 random numbers between 100 and 
# 200 inclusive.
#
# ============================================================================

import random

def main():
	rand = random.sample(range(100,200),5)
	print(rand)

if __name__=="__main__":
	main()