# ================================================================================== 
#
# Author: 	Zachary Homen
# Date:		09/02/2020
#
# ==================================================================================
#
# Write a program that computes the net amount of a bank account based a transaction 
# log from console input. The transaction log format is shown as following:
#
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
#
# D 300
# D 300
# W 200
# D 100
#
# Then, the output should be:
#
# 500
#
# ==================================================================================

def main():

	total=0
	while True:
		line = input().split()
		if not line:
			break

		if line[0] == 'D':
			total += int(line[1])
		elif line[0] == 'W':
			total -= int(line[1])
		else:
			pass

	print(total)

if __name__=="__main__":
	main()