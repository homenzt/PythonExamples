# ================================================================================== 
#
# Author: 	Zachary Homen
# Date:		09/02/2020
#
# ==================================================================================
#
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the 
# value of a.
#
# Suppose the following input is supplied to the program:
#
# 9
#
# Then, the output should be:
#
# 11106
#
# ==================================================================================

def main():
	dig = input()
	tmp = ''
	result = 0

	for i in range(4):
		tmp = dig + tmp
		result += int(tmp)
	print(result)

if __name__=="__main__":
	main()