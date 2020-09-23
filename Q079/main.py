# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/23/2020
#
# ============================================================================
#
# Please write a program to generate all sentences where subject is in ["I", 
# "You"] and verb is in ["Play", "Love"] and the object is in 
# ["Hockey","Football"].
#
# ============================================================================

def main():
	subjects = ["I", "You"]
	verbs = ["Play", "Love"]
	objects = ["Hockey", "Football"]

	for i in subjects:
		for j in verbs:
			for k in objects:
				print(i + " " + j + " " + k + ".")

if __name__=="__main__":
	main()