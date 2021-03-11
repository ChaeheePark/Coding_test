x=int(input())
s=[]
for i in range(x):
    t=int(input())
    s.append(t)
    if t==0:
        s.pop()
        s.pop()
print(sum(s))
