#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        new_list = [0]

    new_list = my_list.copy()
    new_list.sort()

    sum = new_list[0]
    cur_num = new_list[0]

    for num in new_list:
        if num > cur_num:
            sum += num
            cur_num = num
    return (sum)
