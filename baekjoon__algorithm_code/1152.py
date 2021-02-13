x=input()
l=x.split(' ')
cnt=0
for i in range(len(l)):
    if l[i]=="":
        cnt+=1
print(len(l)-cnt)
