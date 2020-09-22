# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/22/2020
#
# ============================================================================
#
# Write a program to compute:
#
# f(n)=f(n-1)+100 when n>0
# and f(0)=0
#
# with a given n input by console (n>0).
#
# Example: If the following n is given as input to the program:
#
# 5
#
# Then, the output of the program should be:
#
# 500
#
# In case of input data being supplied to the question, it should be assumed to 
# be a console input.
#
# ============================================================================

def function(n):
	if n == 0:
		return 0
	else:
		return function(n-1)+100

def main():
	n = int(input())
	print(function(n))

if __name__=="__main__":
	main()