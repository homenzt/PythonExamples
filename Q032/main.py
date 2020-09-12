# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/12/2020
#
# ============================================================================
#
# Define a function which can generate a dictionary where the keys are 
# numbers between 1 and 20 (both included) and the values are square of keys. 
# The function should just print the keys only.
#
# ============================================================================

def square():
	mydict = dict()
	for i in range(1,21):
		mydict[i] = i**2
	print(*mydict.keys(),sep=",")

def main():
	square()
	
if __name__=="__main__":
	main()