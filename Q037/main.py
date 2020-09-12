# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/12/2020
#
# ============================================================================
#
# Define a function which can generate and print a tuple where the value are 
# square of numbers between 1 and 20 (both included).
#
# ============================================================================

def square():
	items = list()
	for i in range(1,21):
		items.append(i**2)
	print(*tuple(items),sep=",")

def main():
	square()
	
if __name__=="__main__":
	main()