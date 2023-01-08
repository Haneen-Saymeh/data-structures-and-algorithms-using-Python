def selection_sort(my_list):
    for i in range(0, len(my_list)-1):
        min = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min]:
                min=j
        if min !=i:
            my_list[min], my_list[i] = my_list[i], my_list[min]
    return my_list


print(selection_sort([9,8,5,7,4,6]))