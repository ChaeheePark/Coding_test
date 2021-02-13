def solution(n):
    answer = 0
    t=[]
    t=str(n)
    for i in range(len(t)):
        answer+=int(t[i])
    return answer
