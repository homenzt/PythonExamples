# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/22/2020
#
# ============================================================================
#
# Please write a program using generator to print the even numbers between 0 and 
# n in comma separated form while n is input by console.
#
# Example: If the following n is given as input to the program:
#
# 10
#
# Then, the output of the program should be:
#
# 0,2,4,6,8,10
#
# In case of input data being supplied to the question, it should be assumed to 
# be a console input.
#
# ============================================================================

def evens(n):
	
	for i in range(n+1):
		if i%2==0:
			yield i

def main():

	ans = list()
	n = int(input())
	
	for i in evens(n):
		ans.append(str(i))

	print(*ans,sep=',')

if __name__=="__main__":
	main()