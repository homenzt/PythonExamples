# Author: 	zhomen
# Date:		08/31/2020
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

def main():
	nums = input("Enter a list of comma seperated numbers: ")
	l = nums.split(',')
	t = tuple(l)
	print(l)
	print(t)

if __name__=="__main__":
	main()