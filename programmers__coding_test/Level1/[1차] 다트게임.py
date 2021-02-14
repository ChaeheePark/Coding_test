def solution(dartResult):
    length=len(dartResult)
    answer=0
    temp=[0,0,0,0]
    j=0
    cnt=0
    for i in range(length):
        t=dartResult[i]
        if t.isdigit():
           
            if cnt==1:
                temp[j]=10
                cnt=0
            else:
                temp[j]=int(t)
            if dartResult[i+1]=='S':
                temp[j]=temp[j]*1
            elif dartResult[i+1]=='D':
                temp[j]=temp[j]*temp[j]
            elif dartResult[i+1]=='T':
                temp[j]=temp[j]*temp[j]*temp[j]
            else:
                cnt+=1
                
        else : #문자열인경우
            if t=='#':
                answer-=temp[j-1]
                temp[j-1]=temp[j-1]*(-1)
                answer+=temp[j-1]
                
            elif t=='*':
                answer-=temp[j-1]+temp[j-2]
                temp[j-1]=temp[j-1]*2
                temp[j-2]=temp[j-2]*2
                answer+=temp[j-1]+temp[j-2]    
            else:
                answer+=temp[j]
                
                j+=1
               
    return answer
