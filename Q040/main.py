# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/20/2020
#
# ============================================================================
#
# Write a program which accepts a string as input to print "Yes" if the 
# string is "yes" or "YES" or "Yes", otherwise print "No".
#
# ============================================================================

def main():
	strin = input()
	correct = ["Yes", "yes", "YES"]
	if strin in correct:
		print("Yes")
	else:
		print("No")
	
if __name__=="__main__":
	main()