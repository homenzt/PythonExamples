# ================================================================================== 
#
# Author: 	Zachary Homen
# Date:		09/02/2020
#
# ==================================================================================
#
# Write a program that accepts a sequence of whitespace separated words as input and 
# prints the words after removing all duplicate words and sorting them 
# alphanumerically.
#
# Suppose the following input is supplied to the program:
#
# hello world and practice makes perfect and hello world again
#
# Then, the output should be:
#
# again and hello makes perfect practice world
#
# ==================================================================================

def main():
	words = input().split(" ")
	lst = list(set(words))
	lst.sort()
	print(*lst, sep=" ")

if __name__=="__main__":
	main()