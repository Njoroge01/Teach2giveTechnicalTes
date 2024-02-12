#Reverse Integer
def reverse_integer(num):  
    num_str = str(num)
    if num_str[0] == '-':
    
        reversed_num = int('-' + num_str[:0:-1])
    else:
        reversed_num = int(num_str[::-1])
    
    return reversed_num
print(reverse_integer(500))  
print(reverse_integer(-56))   
print(reverse_integer(-90))   
print(reverse_integer(91))    
