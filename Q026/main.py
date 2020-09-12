# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/10/2020
#
# ============================================================================
#
# Define a function which can compute the sum of two numbers.
#
# ============================================================================

def add(a,b):
	return int(a)+int(b)

def main():
	nums = input().split(",")
	print(add(nums[0],nums[1]))

	
if __name__=="__main__":
	main()