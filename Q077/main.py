# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/23/2020
#
# ============================================================================
#
# Please write a program to compress and decompress the string "hello world!hello 
# world!hello world!hello world!".
#
# ============================================================================

from timeit import Timer

def main():
	print(Timer("for i in range(100): 1+1").timeit())

if __name__=="__main__":
	main()