def solution(s):
    li=s.split(" ")
    answer=[]
    
    for i in range(len(li)):
        a=li[i]
        a=a.capitalize()
        answer.append(a)
    return ' '.join(answer)
