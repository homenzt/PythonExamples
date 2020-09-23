# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/23/2020
#
# ============================================================================
#
# Please write a program to randomly generate a list with 5 even numbers between 
# 100 and 200 inclusive.
#
# ============================================================================

import random

def main():
	rand = random.sample([i for i in range(100,200) if i%2==0],5)
	print(rand)

if __name__=="__main__":
	main()