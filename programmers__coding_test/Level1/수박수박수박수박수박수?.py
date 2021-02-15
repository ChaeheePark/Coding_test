def solution(n):
    answer=''
    if(n%2!=0): #홀수일때
        answer='수'
        if(n>1):
            for i in range(n//2):
                answer+='박수'
    else:
        for i in range (n//2):
            answer+='수박'
    return answer
    
