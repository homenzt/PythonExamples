# ============================================================================
#
# Author: 	Zachary Homen
# Date:		09/22/2020
#
# ============================================================================
#
# Please write a binary search function which searches an item in a sorted list. 
# The function should return the index of element to be searched in the list.
#
# ============================================================================

import math


# Need to fix
def bin_search(li, element):

    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif int(li[mid])>int(element):
            top = mid-1
        else:
            bottom = mid+1

    return index


def main():

	n = input()
	li = [2,5,7,8,11,17,222]

	print(bin_search(li,n))

if __name__=="__main__":
	main()