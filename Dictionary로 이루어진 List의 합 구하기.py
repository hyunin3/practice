list_dict = [{'name': 'kim', 'age': 12},
             {'name': 'lee', 'age': 4} ]  

def dict_list_sum(lst):
    sum = 0
    for dic in lst:
        sum = sum + dic['age']
    return sum

print(dict_list_sum(list_dict))    