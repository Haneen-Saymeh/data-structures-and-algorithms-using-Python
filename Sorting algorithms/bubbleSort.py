def bubble(my_list):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(my_list)-1):

            if my_list[i] > my_list[i+1]:
                sorted=False
                my_list[i], my_list[i+1]= my_list[i+1],my_list[i]
    return my_list

print(bubble([8,9,7,5,2,4]))
                