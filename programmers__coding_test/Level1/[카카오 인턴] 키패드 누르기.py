def solution(numbers, hand):
    answer = ''
    temp=-1
    for i in range(len(numbers)):
        if numbers[i]==1 or numbers[i]==4 or numbers[i]==7:
            temp=0 #0은 left 1은 right
            answer+='L'
        elif numbers[i]==3 or numbers[i]==6 or numbers[i]==9:
            temp=1
            answer+='R'
        else:
            if temp==1:
                answer+='R'
            elif temp==0:
                answer+='L'
            else:
                if hand == 'left':
                    answer+='L'
                else:
                    answer+='R'
    return answer
