# ================================================================================== 
#
# Author: 	Zachary Homen
# Date:		09/02/2020
#
# ==================================================================================
#
# Write a program, which will find all such numbers between 1000 and 3000 (both 
# included) such that each digit of the number is an even number.The numbers
# obtained should be printed in a comma-separated sequence on a single line.
#
# ==================================================================================

def main():
	result = []
	for i in range(1000,3001):
		even = True
		for j in str(i):
			if int(j)%2==1:
				even = False
		if even:
			result.append(i)
	print(*result, sep=",")

if __name__=="__main__":
	main()