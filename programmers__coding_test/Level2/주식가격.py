from collections import deque

def solution(prices):
    answer=[]
    prices=deque(prices)
    j=0
    while prices:
        t=prices.popleft()
        answer.append(0)
        for i in prices:
            answer[j]+=1
            if t>i:
                break
        j+=1
    return answer
