num = int(input())
def sum_of_digit1(num):
    sum=0
    for i in list(str(num)):
        sum=sum+int(i)
    return sum

print(sum_of_digit1(num))


num = str(num)
def sum_of_digit2(num):
    if num == '':
        return 0
    return sum_of_digit2((num)[:-1]) + int(num[-1])
print(sum_of_digit2(num))