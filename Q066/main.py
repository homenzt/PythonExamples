# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/22/2020
#
# ============================================================================
#
# Please write a program which accepts basic mathematic expression from console 
# and print the evaluation result.
#
# Example: If the following n is given as input to the program:
#
# 35 + 3
#
# Then, the output of the program should be:
#
# 38
#
# ============================================================================

def main():

	math = input()
	print(eval(math))

if __name__=="__main__":
	main()