x=int(input())
count=0
li=list(map(int,input().split()))
for i in range(x):
    flag=1
    if li[i]>1:
        for j in range(2,li[i]):
            if li[i]%j==0:
                flag=0
                break
        if flag==1:
            count+=1
print(count)
