def solution(n):
    answer = []
    t=str(n)
    for i in range(len(t)):
        answer.append(int(t[len(t)-i-1]))
    return answer
