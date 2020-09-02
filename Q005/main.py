# Author: 	zhomen
# Date:		08/31/2020
# Define a class which has at least two methods:
#  - getString: to get a string from console input
#  - printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class IOstring():

	def getString(self):
		self.s = input()

	def printString(self):
		print(self.s.upper())


def main():
	xx = IOstring()
	xx.getString()
	xx.printString()


if __name__=="__main__":
	main()