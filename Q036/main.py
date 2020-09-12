# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/12/2020
#
# ============================================================================
#
# Define a function which can generate a list where the values are square of 
# numbers between 1 and 20 (both included). Then the function needs to print 
# all values except the first 5 elements in the list.
#
# ============================================================================

def square():
	items = list()
	for i in range(1,21):
		items.append(i**2)
	print(*items[5:],sep=",")

def main():
	square()
	
if __name__=="__main__":
	main()