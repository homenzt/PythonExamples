# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/22/2020
#
# ============================================================================
#
# Write a program to read an ASCII string and to convert it to a unicode string 
# encoded by utf-8.
#
# ============================================================================

def main():

	asciistring = "hello world"
	unistring = asciistring.encode('utf-8')
	print(unistring)

if __name__=="__main__":
	main()