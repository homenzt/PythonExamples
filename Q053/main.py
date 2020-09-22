# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/22/2020
#
# ============================================================================
#
# Assuming that we have some email addresses in the "username@companyname.com" 
# format, please write program to print the user name of a given email address. 
# Both user names and company names are composed of letters only.
#
# Example: If the following email address is given as input to the program:
#
# john@google.com
#
# Then, the output of the program should be:
#
# john
# 
# In case of input data being supplied to the question, it should be assumed to 
# be a console input.
#
# ============================================================================

def main():

	mail = input().split("@")
	print(mail[0])

if __name__=="__main__":
	main()