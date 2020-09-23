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

import zlib

def main():

	s = "hello world!hello world!hello world!hello world!"
	y = bytes(s, 'utf-8')
	t = zlib.compress(y)
	
	print(t)
	print(zlib.decompress(t))

if __name__=="__main__":
	main()