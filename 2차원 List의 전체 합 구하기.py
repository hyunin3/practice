list_a = [[1], [2,3], [4,5,6], [7,8,9,10]]

def all_list_sum(lst):
    sum = 0
    for sub_lst in lst:
        for i in sub_lst:
            sum = sum + i
    return sum

print(all_list_sum(list_a))            

