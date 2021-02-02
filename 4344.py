c=int(input())
for _ in range(c):
    l=list(map(int, input().split(' ')))
    cnt=0
    avg=sum(l[1:])/(len(l)-1)
    for j in range(1,len(l)):
        if l[j]>avg:
            cnt+=1
    print('%0.3f%%'%((cnt/l[0])*100))

 
