list_a = [1, 2, 3, 4, 5]

def list_sum(lst):
    sum = 0
    for i in lst:
        sum = sum + i
    return sum

print(list_sum(list_a))        