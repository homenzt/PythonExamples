# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/22/2020
#
# ============================================================================
#
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by 
# console (n>0).
#
# Example: If the following n is given as input to the program:
#
# 5
#
# Then, the output of the program should be:
#
# 3.55
#
# In case of input data being supplied to the question, it should be assumed to 
# be a console input.
#
# ============================================================================

def main():

	num = int(input())

	ans = 0.0
	for i in range(1,num+1):
		ans += float(float(i)/(i+1))

	print(ans)

if __name__=="__main__":
	main()