#패킹/언패킹

# x,y=1,2,3
# z=1,2,3

# print(z,type(z)) #(1,2,3), 튜플

# a,b=1,2,3,4 #에러

# def my_sum(a,b,c):
#     return a+b+c

# num_list = [10,20,30]

# rlt=my_sum(num_list[0],num_list[1],num_list[2])
# rlt=my_sum(*num_list)

def test(*values):
    for value in values:
        print(value)

test(1)
test(1,2)
test(1,2,3,4) #4개 변수 받음

def test(*args): #가변인자
    rlt=0
    for value in args:
        rlt=rlt+value
    return rlt

my_sum() #0
my_sum(1,2,3) #6   

def test(a,b,*args):
    rlt=0
    for value in args:
        rlt=rlt+value
    return rlt

my_sum() #에러
my_sum(1,2,3) #12는 ab에 들어가고 그 이후 수는 나머지에 들어감

def test(**kwargs):
    print(kwargs, type(kwargs))
    kwargs['name']
    return kwargs

test(name='ai',age=21)#키워드 가변인자   

def test(*args, **kwargs):  #각각 분리해서 들어감

test(1,2,3, music='IU')