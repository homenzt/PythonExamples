# ================================================================================== 
#
# Author: 	Zachary Homen
# Date:		09/02/2020
#
# ==================================================================================
#
# Write a program that accepts a sentence and calculate the number of letters and 
# digits.
#
# Suppose the following input is supplied to the program:
#
# hello world! 123
#
# Then, the output should be:
#
# LETTERS 10
# DIGITS 3
#
# ==================================================================================

def main():
	data = input()

	ltrcnt = 0
	digcnt = 0

	print(data)
	for c in data:
		if str.isalpha(c):
			ltrcnt += 1
		elif str.isdigit(c):
			digcnt += 1
		else:
			pass

	print("LETTERS ",ltrcnt)
	print("DIGITS ",digcnt)

if __name__=="__main__":
	main()