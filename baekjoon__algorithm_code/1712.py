x=input()
li=x.split(" ")
A=int(li[0])
B=int(li[1])
C=int(li[2])
if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))
