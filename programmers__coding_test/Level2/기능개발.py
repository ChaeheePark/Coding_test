import math

def solution(progresses, speeds):
    days=[]
    pro_count=len(progresses)
    for i in range(pro_count):
        days.append(0)
        100
        if ((100-progresses[i])/speeds[i]) % 1>0:
            days[i]=(((100-progresses[i])/speeds[i]) // 1 )+1
        else:
            days[i]=int(((100-progresses[i])/speeds[i]))

    
    answer=[]
    
    while len(days)>0:
        
        t=days.pop(0)
        days_c=days.copy()
        count=1
        
        for i in range(len(days)):
            
            if t>=days[i]:
                count+=1
                days_c.pop(0)
                
            else:
                break
                
        days=days_c.copy()
        answer.append(count)
        
    return answer
