# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/23/2020
#
# ============================================================================
#
# Please write a program to output a random even number between 0 and 10 
# inclusive using random module and list comprehension.
#
# ============================================================================

import random

def main():
	rand = random.choice([i for i in range(11) if i%2==0])
	print(rand)

if __name__=="__main__":
	main()