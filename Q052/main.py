# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/22/2020
#
# ============================================================================
#
# Define a custom exception class which takes a string message as attribute.
#
# ============================================================================

class MyError(Exception):

	def __init__(self,msg):
		self.msg = msg

def attempt():
	return 5/0

def main():

	try:
		attempt()
	except MyError as me:
		print("Error: " + me.msg)

if __name__=="__main__":
	main()