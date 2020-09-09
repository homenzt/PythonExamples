# ==================================================================================
#
# Author: 	Zachary Homen
# Date:		09/09/2020
#
# ==================================================================================
#
# Define a class with a generator which can iterate the numbers, which are divisible 
# by 7, between a given range 0 and n.
#
# Suppose the following input is supplied to the program:
#
# 7
#
# Then, the output should be:
#
# 0
# 7
# 14
#
# ==================================================================================

class Divider():

	def generate(self, n):
		num = 0
		while num < n+1:
			if num%7 == 0: yield num
			num += 1


def main():
	div = Divider()
	gen = div.generate(int(input()))
	print(*gen, sep="\n")

if __name__=="__main__":
	main()