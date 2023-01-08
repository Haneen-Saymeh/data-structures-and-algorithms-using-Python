def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        while my_list[i-1] > my_list[i] and i>0:
            my_list[i], my_list[i-1]= my_list[i-1], my_list[i]
            i=i-1
    return my_list

print(insertion_sort([9,8,7,7,5,6,4,3]))
            