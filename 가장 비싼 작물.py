grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]


def sort_order(i):
    return i[1]
grain_lst.sort(key = sort_order)
#grain_lst.sort(key = lambda i : i[1])

print(grain_lst[-1][0])
