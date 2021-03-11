x=int(input())
s=[]
for i in range(x):
    t=input()
    count=0
    flag=True
    for j in range(len(t)):
        if t[j]=="(":
            count+=1
            
        if t[j]==")":
            if count>=1:
                count-=1
            else:
                flag=False
                break
    if count!=0 or flag==False:
        print("NO")
    else:
        print("YES")
