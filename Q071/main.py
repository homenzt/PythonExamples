# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/23/2020
#
# ============================================================================
#
# Please write a program to output a random number, which is divisible by 5 and 
# 7, between 10 and 150 inclusive using random module and list comprehension.
#
# ============================================================================

import random

def main():
	rand = random.choice([i for i in range(10,150) if i%5==0 and i%7==0])
	print(rand)

if __name__=="__main__":
	main()