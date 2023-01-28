def binarySearch(array, target):
    left = 0
    right = len(array)-1
    while left<=right:
        mid = left+(right-left)//2
        midValue = array[mid]
        if target == midValue:
            return mid
        elif target > midValue:
            left = mid+1
        else:
            right = mid-1
    return None

print(binarySearch([2,3,4,5,6,7,8],5))

