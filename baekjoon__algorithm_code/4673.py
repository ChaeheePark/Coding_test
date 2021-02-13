def d(n):
    sum=0
    t=list(str(n))
    
    for i in range(len(t)):
        sum+=int(t[i])
    return sum+n
a=[]
for i in range(1,10001):
    p=d(i)
    a.append(p)
    
for i in range(1,10001):
    if i not in a:
        print(i)
