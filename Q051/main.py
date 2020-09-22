# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/22/2020
#
# ============================================================================
#
# Write a function to compute 5/0 and use try/except to catch the exceptions.
#
# ============================================================================

def attempt():
	return 5/0

def main():
	try:
		attempt()
	except ZeroDivisionError:
		print("Failed: Because you divided by zero.")
	except:
		print("Any other exception")

if __name__=="__main__":
	main()