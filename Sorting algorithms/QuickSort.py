def quick_sort(my_list):
    length = len(my_list)
    if length < 1 :
        return my_list 
    else:
        pivot = my_list.pop()

    greater_items=[]
    lower_items=[]

    for item in my_list:
        if item > pivot:
            greater_items.append(item)
        else:
            lower_items.append(item)

    return quick_sort(lower_items) + [pivot] + quick_sort(greater_items)


print(quick_sort([5,7,8,9,1,5,10,4,3,6]))