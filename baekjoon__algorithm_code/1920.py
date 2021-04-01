x=int(input())
li=set(map(int,input().split()))
y=int(input())
lii=list(map(int,input().split()))

for i in lii:
    if i in li:
        print(1)
    else:
        print(0)
