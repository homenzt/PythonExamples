# ================================================================================== 
#
# Author: 	Zachary Homen
# Date:		09/01/2020
#
# ==================================================================================
#
# Write a program that accepts sequence of lines as input and prints the lines after 
# making all characters in the sentence capitalized.
#
# Suppose the following input is supplied to the program:
#
# Hello world
# Practice makes perfect
#
# Then, the output should be:
#
# HELLO WORLD
# PRACTICE MAKES PERFECT
#
# ==================================================================================

def main():

	lines=[]
	while True:
		line = input()
		if line:
			lines.append(line.upper())
		else:
			break
	txt = '\n'.join(lines)
	print(txt)

if __name__=="__main__":
	main()