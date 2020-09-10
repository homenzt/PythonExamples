# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/09/2020
#
# ============================================================================
#
# Write a method which can calculate square value of number
#
# ============================================================================

class Square():

	def calculate(self,n):
		print(n**2)


def main():

	num = input()

	maths = Square()
	maths.calculate(int(num))

if __name__=="__main__":
	main()