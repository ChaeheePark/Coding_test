x=int(input())
count=0
while(1):
    if x%5==0:
        count+=x//5
        print(count)
        break
    x-=3
    count+=1
    if x<0:
        print(-1)
        break
