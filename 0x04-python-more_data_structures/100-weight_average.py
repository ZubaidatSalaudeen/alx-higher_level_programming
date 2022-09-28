#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    nom, denom = 0, 0
    for i in range(0, len(my_list)):
        nom += (my_list[i][0] * my_list[i][1])
        denom += my_list[i][1]
    return (nom / denom)
