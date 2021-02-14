def solution(n, arr1, arr2):
    answer=[]
    for i in range(n):
        
        #원소1개 2진수로 바꾸기
        b1=format(arr1[i],'b')
        b2=format(arr2[i],'b')
        b1=list(b1)
        b2=list(b2)
        while(len(b1)!=n):
            b1.insert(0,'0')
        while(len(b2)!=n):
            b2.insert(0,'0')
        print(b1,b2)
        answer.insert(i,'')

        for j in range(n):            
            if b1[j]=='1' or b2[j]=='1':
               answer[i]+='#'
            else:
               answer[i]+=' '
    return answer
