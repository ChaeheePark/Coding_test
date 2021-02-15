def solution(phone_number):
    phone_num=list(phone_number)
    for i in range(0,len(phone_num)-4):
        phone_num[i]='*'
    return ''.join(phone_num)
