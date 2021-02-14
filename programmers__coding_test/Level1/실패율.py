def solution(N, stages):
    answer = {}
    length=len(stages)
    for i in range(1,N+1):
        count=0
        if length==0:
            answer[i]=0
            continue
        for j in range(len(stages)):
            if i==stages[j]:
                count+=1
        answer[i]=(count/length)
        length-=count
    return sorted(answer,key=lambda x:answer[x], reverse=True)
