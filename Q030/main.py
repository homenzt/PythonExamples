# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/12/2020
#
# ============================================================================
#
# Define a function that can accept two strings as input and print the string 
# with maximum length in console. If two strings have the same length, then 
# the function should print all strings line by line.
#
# ============================================================================

def longer(a,b):
	if len(a) > len(b):
		print(a)
	elif len(b) > len(a):
		print(b)
	else:
		print(a)
		print(b)

def main():
	longer("This is one string"," and this is the other")
	
if __name__=="__main__":
	main()