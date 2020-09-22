# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/22/2020
#
# ============================================================================
#
# Write a special comment to indicate a Python source code file is in unicode.
#
# ============================================================================

def main():

	asciistring = "hello world"
	unistring = asciistring.encode('utf-8')
	# -*- coding: utf-8 -*-
	print(unistring)

if __name__=="__main__":
	main()