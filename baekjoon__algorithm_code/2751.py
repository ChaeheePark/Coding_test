t=int(input())
li=[]
for i in range(t):
    x=int(input())
    li.append(x)
li.sort()
for i in range(len(li)):
    print(li[i])
