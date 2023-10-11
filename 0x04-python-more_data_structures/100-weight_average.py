#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_sum = 0
    total_weight = 0
    for item in my_list:
        total_sum += (item[0] * item[1])
        total_weight += item[-1]
    return total_sum / total_weight
