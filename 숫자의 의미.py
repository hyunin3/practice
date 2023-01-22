list_a = [83,115,65,102,89]
def get_secret_number(lst):
    result = ' '
    for i in lst:
        result = result + chr(i)
    return result

print(get_secret_number(list_a))        
