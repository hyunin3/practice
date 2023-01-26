# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 

numbers = input() #'------970103-1234567' 

# striped_nubers = numbers.strip('-') #문자열은 리스트랑 달리 바뀔 수 없어서 다른거 
# print(striped_nubers)            #지정해줘야됨

replaced_number = numbers.replace('-', '')
#print(replaced_number)
rereplaced_number = replaced_number.replace(replaced_number[6:13], '*******')   
print(rereplaced_number)