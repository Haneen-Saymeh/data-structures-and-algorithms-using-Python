# Find nth largest number

def nth_large(list, i):
    list = sorted(list, reverse=True)
    print(list[i-1])

nth_large([1,5,8,2,9,4],2)
