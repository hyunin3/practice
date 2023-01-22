def my_func(n):
    return n*10

my_lst=[1,2,3,4,5]

# for i in my_lst:
#     lst=[my_func(i)]
#     print(lst)    


rlt=map(my_func,my_lst)
print(list(rlt))