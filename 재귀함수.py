# def recur():
#     print('뿅')
#     recur()

def fac(n):
    if n == 0:
        return 1
    
    return n * fac(n - 1)

print(fac(5))