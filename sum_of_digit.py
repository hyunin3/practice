#sum_of_digit(3904) # 16
# num = int(input())
# def sum_of_digit1(num):
#     sum=0
#     for i in list(str(num)):
#         sum=sum+int(i)
#     return sum

# print(sum_of_digit1(num))

#def sum_of_digit2(num):
#멈추는 조건이 필요. 멈추는 조건을 맞추기 위해 args바꿔야함    전의 상태를 가지고 나의 상태 설명 가능해야
#n + n-1 + ....+ 2 + 1 + 0
def func(n):
    if n == 0:
        return #0을 만나면 끝남
    print(n) 
    func(n-1)
func(10)

#f(n+1) = f(n) + n+1
def func(n):
    if n:
        return n
    return func(n-1)+n
#1234넣으면  
func(n) = func(n-1) + 4 

def func(number):
    if number == '':   #몫 quoient= number //10    if quoient == 0
        return 0       #나머지 remainder= number % 10  return remainder
    return func(number[:-1]) + int(number[-1]) 마지막
#   10으로 나눈 몫             10으로 나눈 나머지
print(func('1234'))