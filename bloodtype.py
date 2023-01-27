blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
for i in blood_types:
    if i == 'A': 
        cnt1 = cnt1 + 1
    elif i == 'B': 
        cnt2 = cnt2 + 1
    elif i == 'AB': 
        cnt3 = cnt3 + 1
    elif i == 'O': 
        cnt4 = cnt4 + 1 
    my_dic = {'A': cnt1, 'B': cnt2, 'AB': cnt3, 'O': cnt4}               

print(my_dic)