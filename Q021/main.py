# ==================================================================================
#
# Author: 	Zachary Homen
# Date:		09/09/2020
#
# ==================================================================================
#
# A robot moves in a plane starting from the original point (0,0). The robot can 
# move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot 
# movement is shown as the following:
#
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
#
# The numbers after the direction are steps. Please write a program to compute the 
# distance from current position after a sequence of movement and original point. If 
# the distance is a float, then just print the nearest integer. Example: If the 
# following tuples are given as input to the program:
#
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
#
# Then, the output of the program should be:
#
# 2
#
# ==================================================================================

from math import sqrt

def main():

	directions = dict(
		UP=0,
		DOWN=0,
		LEFT=0,
		RIGHT=0
	)

	lines=[]
	while True:
		line = input().split(" ")
		if line != [''] and line[0] in directions:
			directions[line[0]] = directions[line[0]] + int(line[1])
		else:
			break

	result = int(sqrt((directions['UP'] - directions['DOWN'])**2 + (directions['LEFT'] - directions['RIGHT'])**2))
	print(result)

if __name__=="__main__":
	main()