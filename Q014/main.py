# ================================================================================== 
#
# Author: 	Zachary Homen
# Date:		09/02/2020
#
# ==================================================================================
#
# Write a program that accepts a sentence and calculate the number of upper case 
# letters and lower case letters.
#
# Suppose the following input is supplied to the program:
#
# Hello world!
#
# Then, the output should be:
#
# UPPER CASE 1
# LOWER CASE 9
#
# ==================================================================================

def main():
	s = input()

	ucase,lcase = 0,0

	for c in s:
		if c.isupper():
			ucase += 1
		elif c.islower():
			lcase += 1
		else:
			pass

	print("UPPER CASE ",ucase)
	print("LOWER CASE ",lcase)

if __name__=="__main__":
	main()