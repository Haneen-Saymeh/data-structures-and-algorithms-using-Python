# Given an array that consists of elements from range 1 to n. One of the elements is missing from the given list. Find the missing number in the given array.
# example:
# arr=[1,3,5,2,6,4,8,9,10].
# output: the missing number is  7.

def missingnum(list):
    list = sorted(list)
    for x in range  (list[1], len(list)):

        if x not in list:
            print(x)

missingnum([1,3,5,2,6,4,8,9,10])
